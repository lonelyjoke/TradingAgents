@echo off
setlocal
set "SCRIPT_DIR=%~dp0"
set "REPO_ROOT=%SCRIPT_DIR%.."
set "PYTHON_EXE=%PYTHON%"
if "%PYTHON_EXE%"=="" set "PYTHON_EXE=python"
"%PYTHON_EXE%" "%REPO_ROOT%\scripts\preprocess_knowledge_planet.py" %*
endlocal
