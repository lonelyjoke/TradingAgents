@echo off
setlocal

set "REPO_ROOT=%~dp0.."
set "QUANT_PYTHON=%USERPROFILE%\.conda\envs\quant\python.exe"
set "BUNDLED_PYTHON=%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
set "LAUNCHER=%REPO_ROOT%\scripts\generate_knowledge_planet_daily_interactive.py"

if exist "%QUANT_PYTHON%" (
  "%QUANT_PYTHON%" "%LAUNCHER%"
) else if exist "%BUNDLED_PYTHON%" (
  "%BUNDLED_PYTHON%" "%LAUNCHER%"
) else (
  python "%LAUNCHER%"
)
