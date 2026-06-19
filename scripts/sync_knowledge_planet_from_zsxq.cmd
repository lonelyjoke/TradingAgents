@echo off
setlocal

set "REPO_ROOT=%~dp0.."
set "QUANT_PYTHON=%USERPROFILE%\.conda\envs\quant\python.exe"
set "BUNDLED_PYTHON=%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
set "SYNC_SCRIPT=%REPO_ROOT%\scripts\sync_knowledge_planet_from_zsxq.py"

if exist "C:\Program Files\nodejs\node.exe" (
  set "PATH=C:\Program Files\nodejs;%APPDATA%\npm;%PATH%"
)

if exist "%QUANT_PYTHON%" (
  "%QUANT_PYTHON%" "%SYNC_SCRIPT%" %*
) else if exist "%BUNDLED_PYTHON%" (
  "%BUNDLED_PYTHON%" "%SYNC_SCRIPT%" %*
) else (
  python "%SYNC_SCRIPT%" %*
)

endlocal
