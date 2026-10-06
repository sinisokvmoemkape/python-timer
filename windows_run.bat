@echo off


python -m venv venv

echo [1/2] Устанавливаем библиотеки из requirements.txt...

call venv\Scripts\activate.bat
pip install -r requirements.txt

echo [2/2] Все настроено навсегда!



call venv\Scripts\activate.bat
python timer.py
pause
