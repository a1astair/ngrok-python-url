@echo off
pushd %~dp0
START /b cmd /c "ngrok tcp 3389"
START /b cmd /c py -3 ./getNgrokUrl.py"