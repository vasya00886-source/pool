import subprocess
import os
import json
from pygments import highlight
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.formatters import HtmlFormatter

class ChatEngine:
    def __init__(self, router):
        try:
            self.router = router
            self.history = []
        except Exception as e:
            print(f"Ошибка при инициализации ChatEngine: {e}")

    def stream(self, prompt, model):
        try:
            url = f"http://localhost:11434/api/chat"
            headers = {'Content-Type': 'application/json'}
            data = json.dumps({
                "prompt": prompt,
                # Дополнительные поля данных
            })
            request = urllib.request.Request(url, data.encode('utf-8'), headers=headers)
            response = urllib.request.urlopen(request)
            return response.read().decode('utf-8')
        except Exception as e:
            print(f"Ошибка при выполнении запроса: {e}")

    def execute(self, code, lang):
        try:
            if lang == 'python':
                result = subprocess.run(['python', '-c', code], capture_output=True, text=True)
            elif lang == 'rust':
                temp_file = 'temp.rs'
                with open(temp_file, 'w') as f:
                    f.write(code)
                compile_result = subprocess.run(['rustc', temp_file], capture_output=True, text=True)
                if compile_result.returncode != 0:
                    return compile_result.stdout, compile_result.stderr
                try:
                    result = subprocess.run('./temp', capture_output=True, text=True)
                finally:
                    os.remove(temp_file)  # Удаляем временный файл после выполнения
            elif lang == 'go':
                temp_file = 'temp.go'
                with open(temp_file, 'w') as f:
                    f.write(code)
                result = subprocess.run(['go', 'run', temp_file], capture_output=True, text=True)
                os.remove(temp_file)  # Удаляем временный файл после выполнения
            else:
                raise ValueError(f"Неизвестный язык программирования: {lang}")
            
            return result.stdout, result.stderr
        except Exception as e:
            print(f"Ошибка при выполнении кода: {e}")

    def browse(self, path):
        try:
            with open(path, 'r') as f:
                code = f.read()
            highlighted_code = self.highlight(code)
            return highlighted_code
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")

    def highlight(self, code):
        try:
            lexer = guess_lexer(code)  # Используем анализ содержимого для определения языка
            formatter = HtmlFormatter()
            return highlight(code, lexer, formatter)
        except Exception as e:
            print(f"Ошибка при подсветке кода: {e}")

    def save_hist(self, path):
        try:
            with open(path, 'w') as f:
                json.dump(self.history, f)
        except Exception as e:
            print(f"Ошибка при сохранении истории: {e}")