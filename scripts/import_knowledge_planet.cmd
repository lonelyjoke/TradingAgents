@echo off
setlocal

set "REPO_ROOT=%~dp0.."
set "BUNDLED_PYTHON=%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
set "IMPORT_SCRIPT=%REPO_ROOT%\scripts\import_knowledge_planet.py"

if exist "%BUNDLED_PYTHON%" (
  "%BUNDLED_PYTHON%" "%IMPORT_SCRIPT%" %*
) else (
  python "%IMPORT_SCRIPT%" %*
)
