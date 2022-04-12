"""
Модуль 2. Домашнее задание №11
Приложение на Flask.
"""

# Импорт Flask и функций.
from flask import Flask
import utils

app = Flask(__name__)


 # Запуск веб-приложения.
if __name__ == "__main__":
    app.run(debug=True)
