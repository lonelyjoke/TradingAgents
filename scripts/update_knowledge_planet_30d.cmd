@echo off
setlocal

set "REPO_ROOT=%~dp0.."
set "QUANT_PYTHON=%USERPROFILE%\.conda\envs\quant\python.exe"
set "BUNDLED_PYTHON=%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
set "UPDATE_SCRIPT=%REPO_ROOT%\scripts\update_knowledge_planet_30d.py"

if exist "C:\Program Files\nodejs\node.exe" (
  set "PATH=C:\Program Files\nodejs;%APPDATA%\npm;%PATH%"
)

if exist "%QUANT_PYTHON%" (
  "%QUANT_PYTHON%" "%UPDATE_SCRIPT%" %*
) else if exist "%BUNDLED_PYTHON%" (
  "%BUNDLED_PYTHON%" "%UPDATE_SCRIPT%" %*
) else (
  python "%UPDATE_SCRIPT%" %*
)

endlocal
