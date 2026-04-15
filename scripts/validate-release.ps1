$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot

Write-Host "[1/3] Validating gameplay package example..."
python "$root\\skills\\gameplay-design-orchestrator\\scripts\\validate_gameplay_package.py" `
  --package-dir "$root\\examples\\gyro-battle\\final-package"

Write-Host "[2/3] Validating full spec example..."
python "$root\\skills\\game-design-spec\\scripts\\validate_spec.py" `
  --task-dir "$root\\examples\\gyro-battle\\final-spec"

Write-Host "[3/3] Validating execution plan example..."
python "$root\\skills\\game-design-execution-compiler\\scripts\\validate_execution_plan.py" `
  --plan-dir "$root\\examples\\gyro-battle\\final-execution-plan"

Write-Host "[4/4] Smoke-testing execution runner..."
$tmpDir = Join-Path $root "tmp-runner-validation"
if (Test-Path $tmpDir) {
  Remove-Item -Recurse -Force $tmpDir
}
New-Item -ItemType Directory -Path $tmpDir | Out-Null
Copy-Item "$root\\examples\\gyro-battle\\final-execution-plan\\execution-plan.json" "$tmpDir\\execution-plan.json"
Copy-Item "$root\\examples\\gyro-battle\\final-execution-plan\\execution-plan.md" "$tmpDir\\execution-plan.md"
python "$root\\skills\\game-design-execution-runner\\scripts\\run_execution_plan.py" `
  init --plan-dir "$tmpDir" --repo-root "$root" --branch "main"
python "$root\\skills\\game-design-execution-runner\\scripts\\run_execution_plan.py" `
  next --plan-dir "$tmpDir" --format json
python "$root\\skills\\game-design-execution-runner\\scripts\\run_execution_plan.py" `
  handoff --plan-dir "$tmpDir" --format markdown
python "$root\\skills\\game-design-execution-runner\\scripts\\run_execution_plan.py" `
  start --plan-dir "$tmpDir" --task-id "TASK-001"
@'
{
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
python "$root\\skills\\game-design-execution-runner\\scripts\\run_execution_plan.py" `
  complete --plan-dir "$tmpDir" --task-id "TASK-001" --evidence-file "$tmpDir\\task-001-evidence.json"
Remove-Item -Recurse -Force $tmpDir

Write-Host "Validation complete."
