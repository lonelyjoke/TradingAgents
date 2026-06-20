@echo off
setlocal

cd /d "%~dp0"
call "%~dp0scripts\generate_knowledge_planet_daily_interactive.cmd"
set "EXIT_CODE=%ERRORLEVEL%"
echo.
pause
exit /b %EXIT_CODE%
