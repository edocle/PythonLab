@echo off
powershell.exe -NoExit -Command "Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process;.\flask_env\Scripts\Activate;python -m flask run"