@echo off
REM Automately Test Runner for Windows
echo Running tests...
robot -d reports/current tests/
pause
