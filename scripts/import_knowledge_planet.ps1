param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Args
)

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$BundledPython = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
$Script = Join-Path $RepoRoot "scripts\import_knowledge_planet.py"

if (Test-Path $BundledPython) {
    & $BundledPython $Script @Args
} else {
    python $Script @Args
}
