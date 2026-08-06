import json
import os
import subprocess
import pathlib
from rich import table

class Diagnostics:
    def __init__(self):
        self.providers = {
            'ollama': {'url': 'http://localhost:11434/api/v1/models', 'api_key': None},
            'openrouter': {'url': 'https://api.openrouter.ai/', 'api_key': 'your_openrouter_api_key'},
            'groq': {'url': 'https://api.groq.com/', 'api_key': 'your_groq_api_key'},
            'cerebras': {'url': 'https://api.cerebras.cloud/', 'api_key': None}
        }

    def check_ollama(self):
        try:
            response = subprocess.check_output(['curl', 'localhost:11434/api/tags'])
            if response:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error checking Ollama: {e}")
            return False

    def check_providers(self):
        # Проверка провайдеров
        for provider, config in self.providers.items():
            if not config['api_key']:
                print(f"API key missing for {provider}. Please provide an API key.")
                return False
        return True

    def check_gpu(self):
        try:
            response = subprocess.check_output(['nvidia-smi'])
            if response:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error checking GPU: {e}")
            return False

    def check_disk(self):
        total, used, free = shutil.disk_usage("/")
        if free < 1073741824:  # Less than 1 GB free
            print("Less than 1 GB of disk space available.")
            return False
        return True

    def health_report(self):
        report_table = table.Table(show_header=True, header_style="bold magenta")
        report_table.add_column("Check", style="dim")
        report_table.add_column("Status")

        checks = {
            "Ollama": self.check_ollama(),
            "Providers": self.check_providers(),
            "GPU": self.check_gpu(),
            "Disk Space": self.check_disk()
        }

        for check, status in checks.items():
            report_table.add_row(check, "Pass" if status else "Fail")

        print(report_table)

    def config_validate(self, config_dict):
        required_keys = ['ollama', 'openrouter', 'groq', 'cerebras']
        missing_keys = [key for key in required_keys if key not in config_dict]
        if missing_keys:
            print(f"Missing keys in configuration: {missing_keys}")
            return False
        return True

    def self_repair(self):
        repairs = {
            "Ollama": self.repair_ollama,
            "Providers": self.repair_providers,
            "GPU": self.repair_gpu,
            "Disk Space": self.repair_disk
        }

        checks = {
            "Ollama": self.check_ollama(),
            "Providers": self.check_providers(),
            "GPU": self.check_gpu(),
            "Disk Space": self.check_disk()
        }

        for check, status in checks.items():
            if not status:
                print(f"Attempting to repair {check}...")
                repairs[check]()

    def repair_ollama(self):
        # Реализация попытки исправления Ollama
        print("Repairing Ollama...")

    def repair_providers(self):
        # Реализация попытки исправления провайдеров
        print("Repairing providers...")

    def repair_gpu(self):
        # Реализация попытки исправления GPU
        print("Repairing GPU...")

    def repair_disk(self):
        # Реализация попытки исправления диска
        print("Repairing disk space...")