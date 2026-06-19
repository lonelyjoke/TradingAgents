@echo off
setlocal

set "REPO_ROOT=%~dp0.."
set "BUNDLED_PYTHON=%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
set "REPORT_SCRIPT=%REPO_ROOT%\scripts\generate_knowledge_planet_daily.py"

if exist "%BUNDLED_PYTHON%" (
  "%BUNDLED_PYTHON%" "%REPORT_SCRIPT%" %*
) else (
  python "%REPORT_SCRIPT%" %*
)
