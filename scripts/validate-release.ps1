$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot

Write-Host "[1/2] Validating gameplay package example..."
python "$root\\skills\\gameplay-design-orchestrator\\scripts\\validate_gameplay_package.py" `
  --package-dir "$root\\examples\\gyro-battle\\final-package"

Write-Host "[2/2] Validating full spec example..."
python "$root\\skills\\game-design-spec\\scripts\\validate_spec.py" `
  --task-dir "$root\\examples\\gyro-battle\\final-spec"

Write-Host "Validation complete."

