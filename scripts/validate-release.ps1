$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot

function Invoke-Checked {
  param(
    [Parameter(Mandatory = $true)]
    [scriptblock]$ScriptBlock
  )

  & $ScriptBlock
  if ($LASTEXITCODE -ne 0) {
    throw "Command failed with exit code $LASTEXITCODE"
  }
}

Write-Host "[1/4] Validating gameplay package example..."
Invoke-Checked {
  python "$root\\skills\\gameplay-design-orchestrator\\scripts\\validate_gameplay_package.py" `
    --package-dir "$root\\examples\\gyro-battle\\final-package"
}

Write-Host "[2/4] Validating full spec example..."
Invoke-Checked {
  python "$root\\skills\\game-design-spec\\scripts\\validate_spec.py" `
    --task-dir "$root\\examples\\gyro-battle\\final-spec"
}

Write-Host "[3/4] Validating execution plan example..."
Invoke-Checked {
  python "$root\\skills\\game-design-execution-compiler\\scripts\\validate_execution_plan.py" `
    --plan-dir "$root\\examples\\gyro-battle\\final-execution-plan"
}

Write-Host "[4/4] Smoke-testing execution runner..."
$tmpDir = Join-Path $root "tmp-runner-validation"
if (Test-Path $tmpDir) {
  Remove-Item -Recurse -Force $tmpDir
}
New-Item -ItemType Directory -Path $tmpDir | Out-Null
Copy-Item "$root\\examples\\gyro-battle\\final-execution-plan\\execution-plan.json" "$tmpDir\\execution-plan.json"
Copy-Item "$root\\examples\\gyro-battle\\final-execution-plan\\execution-plan.md" "$tmpDir\\execution-plan.md"
Invoke-Checked {
  python "$root\\skills\\game-design-execution-runner\\scripts\\run_execution_plan.py" `
    init --plan-dir "$tmpDir" --repo-root "$root" --branch "main"
}
Invoke-Checked {
  python "$root\\skills\\game-design-execution-runner\\scripts\\run_execution_plan.py" `
    next --plan-dir "$tmpDir" --format json
}
Invoke-Checked {
  python "$root\\skills\\game-design-execution-runner\\scripts\\run_execution_plan.py" `
    handoff --plan-dir "$tmpDir" --format markdown
}
Invoke-Checked {
  python "$root\\skills\\game-design-execution-runner\\scripts\\run_execution_plan.py" `
    dispatch --plan-dir "$tmpDir" --output-dir "$tmpDir\\dispatch-TASK-001"
}
if (-not (Test-Path "$tmpDir\\dispatch-TASK-001\\dispatch-manifest.json")) {
  throw "Dispatch manifest was not created."
}
if (-not (Test-Path "$tmpDir\\dispatch-TASK-001\\task-payload.json")) {
  throw "Dispatch payload was not created."
}
if (-not (Test-Path "$tmpDir\\dispatch-TASK-001\\worker-handoff.md")) {
  throw "Dispatch handoff was not created."
}
if (-not (Test-Path "$tmpDir\\dispatch-TASK-001\\completion-evidence.template.json")) {
  throw "Dispatch evidence template was not created."
}
Invoke-Checked {
  python "$root\\skills\\game-design-execution-runner\\scripts\\worker_adapter.py" `
    pickup --dispatch-dir "$tmpDir\\dispatch-TASK-001" --worker-label "smoke-worker"
}
@'
{
  "dispatch_id": "WRONG-DISPATCH-ID",
  "worker_label": "smoke-worker",
  "summary": "Invalid attempt that should be rejected by the dispatch review gate.",
  "changed_files": [
    "src/ui/hud.tsx"
  ],
  "verification_run": [
    {
      "name": "npm run typecheck",
      "result": "pass"
    },
    {
      "name": "browser-check",
      "result": "pass"
    }
  ],
  "acceptance_checklist": [
    {
      "criterion": "HUD renders all required combat regions from the UI task",
      "status": "met"
    }
  ],
  "open_issues": []
}
'@ | Set-Content -Path "$tmpDir\\task-001-invalid-evidence.json" -Encoding utf8
python "$root\\skills\\game-design-execution-runner\\scripts\\worker_adapter.py" `
  complete --dispatch-dir "$tmpDir\\dispatch-TASK-001" --evidence-file "$tmpDir\\task-001-invalid-evidence.json"
if ($LASTEXITCODE -eq 0) {
  throw "Dispatch review gate accepted invalid dispatch evidence."
}
@'
{
  "dispatch_id": "TASK-001-dispatch-1",
  "worker_label": "smoke-worker",
  "summary": "Built the first-pass HUD shell and verified the browser-facing combat layout.",
  "changed_files": [
    "src/ui/hud.tsx"
  ],
  "verification_run": [
    {
      "name": "npm run typecheck",
      "result": "pass"
    },
    {
      "name": "browser-check",
      "result": "pass"
    }
  ],
  "acceptance_checklist": [
    {
      "criterion": "HUD renders all required combat regions from the UI task",
      "status": "met"
    },
    {
      "criterion": "No approved HUD region is silently omitted",
      "status": "met"
    },
    {
      "criterion": "Typecheck passes",
      "status": "met"
    },
    {
      "criterion": "Browser verification passes",
      "status": "met"
    }
  ],
  "open_issues": []
}
'@ | Set-Content -Path "$tmpDir\\task-001-evidence.json" -Encoding utf8
Invoke-Checked {
  python "$root\\skills\\game-design-execution-runner\\scripts\\worker_adapter.py" `
    complete --dispatch-dir "$tmpDir\\dispatch-TASK-001" --evidence-file "$tmpDir\\task-001-evidence.json"
}
Remove-Item -Recurse -Force $tmpDir

Write-Host "Validation complete."
