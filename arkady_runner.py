import json

class CodeRunner:
    def __init__(self):
        try:
            self.langs = {
                'python': 'python',
                'rust': 'rustc',
                'go': 'go run',
                'cpp': 'g++',
                'java': 'javac',
                'bash': 'bash'
            }
        except Exception as e:
            print(f"Ошибка при инициализации CodeRunner: {e}")

    def detect_lang(self, code):
        # Реализация метода detect_lang
        pass

    def run(self, code, lang):
        # Реализация метода run
        pass

    def run_python(self, code):
        # Реализация метода run_python
        pass

    def run_rust(self, code):
        # Реализация метода run_rust
        pass

    def run_go(self, code):
        # Реализация метода run_go
        pass

    def format_output(self, stdout, stderr, exit_code):
        try:
            output = {
                "stdout": stdout.decode('utf-8').strip(),
                "stderr": stderr.decode('utf-8').strip(),
                "exit_code": exit_code
            }
            return json.dumps(output, indent=4)
        except Exception as e:
            print(f"Ошибка при форматировании вывода: {e}")
            return None