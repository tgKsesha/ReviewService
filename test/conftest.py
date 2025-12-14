import sys
import os

# Добавляем корень проекта в PYTHONPATH,
# чтобы тесты могли импортировать review_service.py
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)
