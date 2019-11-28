@echo off
cd %temp%
for /d %%D in (*) do rd /s /q "%%D"
del /f /q *