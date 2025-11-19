<#
Run pytest-bdd acceptance tests (Playwright + pytest-bdd)

Examples:
  .\scripts\bdd_pytest.ps1 -Headed -JUnit -Html
  .\scripts\bdd_pytest.ps1 -Feature tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py
#>

param(
  [switch]$Headed,
  [switch]$JUnit,
  [switch]$Html,
  [string]$Feature = "tests/acceptance/bdd_playwright/test_playwright_pytestbdd.py",
  [switch]$DryRun
)

# Try to activate .venv automatically if present
$venvActivate = Join-Path -Path (Get-Location) -ChildPath ".venv\Scripts\Activate.ps1"
if (Test-Path $venvActivate) {
  Write-Host "Activating venv: $venvActivate"
  . $venvActivate
} else {
  Write-Host "No .venv found at $venvActivate - ensure your virtualenv is active"
}

# HEADLESS control
if ($Headed) {
  Write-Host "Running in HEADED mode (HEADLESS=false)"
  $env:HEADLESS = 'false'
} else {
  Write-Host "Running in HEADLESS mode (HEADLESS=true)"
  $env:HEADLESS = 'true'
}

# Build pytest command
$pytestArgs = @()
$pytestArgs += "--capture=no"   # helpful when debugging
$pytestArgs += "-q"
$pytestArgs += "-x"            # fast-fail: stop on first failure (CI-friendly)
$pytestArgs += "--maxfail=1"  # explicit max-fail for clarity
$pytestArgs += "$Feature"

# Ensure results dir exists if we need it
if ($JUnit -or $Html) {
  $resultsDir = Join-Path (Get-Location) "results"
  if (-not (Test-Path $resultsDir)) { New-Item -ItemType Directory -Path $resultsDir | Out-Null }
}

if ($JUnit) {
  $junitPath = Join-Path $resultsDir "junit.xml"
  $pytestArgs += "--junitxml=`"$junitPath`""
  Write-Host "JUnit output: $junitPath"
}

if ($Html) {
  $htmlPath = Join-Path $resultsDir "report.html"
  $pytestArgs += "--html=`"$htmlPath`""
  $pytestArgs += "--self-contained-html"
  Write-Host "HTML report: $htmlPath"
}

$cmd = "pytest " + ($pytestArgs -join ' ')
if ($DryRun) {
  Write-Host "DRY RUN: $cmd"
  exit 0
}

Write-Host "Running: $cmd"
Invoke-Expression $cmd

# propagate exit code
exit $LASTEXITCODE