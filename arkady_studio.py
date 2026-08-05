from rich.console import Console

class ArkadyStudio:
    def __init__(self):
        self.providers = {
            'ollama': {'url': 'http://localhost:11434/api/v1/models', 'api_key': None},
            # другие провайдеры...
        }
        self.console = Console()

    def show_header(self):
        try:
            header_panel = Panel("ARKADY STUDIO", title="Welcome")
            self.console.print(header_panel)
        except Exception as e:
            print(f"Error showing header: {e}")

    def run(self):
        try:
            while True:
                # Основной цикл программы
                self.show_header()
                # Добавьте другие методы и логику по необходимости
        except KeyboardInterrupt:
            print("Программа завершена.")
        except Exception as e:
            print(f"Ошибка в основном цикле: {e}")