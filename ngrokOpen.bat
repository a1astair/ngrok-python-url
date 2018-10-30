@echo off
START /b cmd /c "ngrok tcp 3389"
START /b cmd /c "python ./getNgrokUrl.py"
exit