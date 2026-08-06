import re

class RegexTester:
    def __init__(self, pattern):
        try:
            self.pattern = re.compile(pattern)
        except Exception as e:
            print(f"Ошибка при компиляции шаблона: {e}")

    def test(self, text):
        try:
            return bool(self.pattern.match(text))
        except Exception as e:
            print(f"Ошибка при тестировании текста: {e}")
            return False

    def findall(self, text):
        try:
            return self.pattern.findall(text)
        except Exception as e:
            print(f"Ошибка при поиске всех совпадений: {e}")
            return []

    def highlight_matches(self, text):
        try:
            matches = self.pattern.findall(text)
            for match in matches:
                print(f"\033[91m{match}\033[0m", end="")
            print()
        except Exception as e:
            print(f"Ошибка при подсветке совпадений: {e}")

    def rich(self, text):
        try:
            from rich.console import Console
            console = Console()
            matches = self.pattern.findall(text)
            for match in matches:
                console.print(match, style="bold red")
        except Exception as e:
            print(f"Ошибка при использовании Rich: {e}")