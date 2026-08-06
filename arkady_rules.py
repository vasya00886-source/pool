import os

class RuleEngine:
    def __init__(self, dev_key):
        self.dev_key = dev_key

    def get_raw(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                raw_data = file.read()
            return raw_data
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return None