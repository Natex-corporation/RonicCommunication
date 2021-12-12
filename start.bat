@echo off
tasklist.exe /V /FI "IMAGENAME eq cmd.exe" /FO LIST | find "beeing online all the time.py" >nul
if ERRORLEVEL 1 (
   echo 0
) else (
    echo 1
)