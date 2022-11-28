@echo off
if not exist venv\ (
echo Setting up virtual environment..
python -m venv venv
cd venv\Scripts
call activate.bat
echo Virtual environment created!
echo Installing required packages...
cd ..
cd ..
@echo off
pip install -r requirements.txt
cls 
python main.py
pause) else (
python main.py
pause)