import json
import os
from pathlib import Path

class I18n:
    def __init__(self, language='RU'):
        self.language = language
        self.translations = {'RU': {
            'Search': 'Поиск',
            'Skills': 'Навыки',
            'Settings': 'Настройки',
            'Chat': 'Чат',
            'Plugins': 'Плагины',
            'Models': 'Модели',
            'Sessions': 'Сессии',
            'Diagnostics': 'Диагностика',
            '3D Visualizer': '3D Визуализатор',
            'Remote': 'Удалённое',
            'Marketplace': 'Магазин',
            'Tokens': 'Токены',
            'Exit': 'Выход',
            'New': 'Новая',
            'Save': 'Сохранить',
            'Load': 'Загрузить',
            'Run': 'Запуск',
            'Stop': 'Стоп',
            'Clear': 'Очистить',
            'Help': 'Помощь'
        }}

    def add_translation(self, key, value, language='RU'):
        try:
            if language not in self.translations:
                raise ValueError(f"Language '{language}' is not supported.")
            
            if key in self.translations[language]:
                raise KeyError(f"Translation for key '{key}' already exists in language '{language}'.")
            
            self.translations[language][key] = value
        except Exception as e:
            print(f"Error: {e}")

# Пример использования
i18n = I18n()
i18n.add_translation('Test', 'Тест')
print(i18n.translations['RU']['Test'])