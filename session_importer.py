import json
from pathlib import Path

class SessionImporter:
            def __init__(self):
                self.target = ArkadyMemory()

            def import_jcode(self, sessions_dir):
                if not Path(sessions_dir).exists():
                    raise FileNotFoundError(f"Directory {sessions_dir} does not exist.")

                try:
                    session_files = list(Path(sessions_dir).glob('session_*.json'))
                    for file in session_files:
                        with open(file, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                            # Реализация обработки данных из JSON
                            self.target.add_session(data)
                except Exception as e:
                    print(f"Ошибка при импорте jcode: {e}")

            def import_ollama_log(self, path):
                try:
                    with open(path, 'r', encoding='utf-8') as file:
                        log_data = file.read()
                        # Реализация парсинга лог-файла для извлечения request и response
                        # Например, предположим, что лог содержит строки в формате "request: ...; response: ..."
                        requests_responses = [line.split(';') for line in log_data.strip().split('\n')]
                        for req_res in requests_responses:
                            request = req_res[0].strip().split(': ')[1]
                            response = req_res[1].strip().split(': ')[1]
                            self.target.add_request_response(request, response)
                except FileNotFoundError:
                    print(f"Файл {path} не найден.")
                except Exception as e:
                    print(f"Ошибка при импорте лога: {e}")

            def run_all(self):
                try:
                    self.import_jcode('sessions')
                    self.import_ollama_log('ollama.log')
                except Exception as e:
                    print(f"Ошибка при выполнении run_all: {e}")