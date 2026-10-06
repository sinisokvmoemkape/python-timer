#!/usr/bin/fish


python -m venv venv

echo "[1/2] Ставим requirements.txt..."
source venv/bin/activate.fish
pip install -r requirements.txt

echo "[2/2] Готово!"



source venv/bin/activate.fish
python timer.py
