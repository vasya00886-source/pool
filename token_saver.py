import json
import hashlib
import re
import time

class TokenSaver:
    def __init__(self):
        self.semantic_cache = {}

    def check_cache(self, prompt):
        # Вычисляем SHA256 хеш для промпта
        prompt_hash = hashlib.sha256(prompt.encode('utf-8')).hexdigest()
        
        # Проверяем наличие хеша в семантическом кэше
        if prompt_hash in self.semantic_cache:
            similar_prompts = self.semantic_cache[prompt_hash]
            return True, similar_prompts
        return False, []

    def estimate_tokens(self, text):
        # Простая оценка количества токенов как длины текста в словах
        words = re.findall(r'\b\w+\b', text)
        return len(words)

    def get_max_tokens(self, task_type):
        if task_type == "code":
            return 512
        elif task_type == "chat":
            return 256
        else:
            raise ValueError("Unknown task type")

    def get_stop_sequences(self):
        # Пример списка stop sequences
        return ["<|endoftext|>", "<<END>>"]

    def token_report(self, text):
        try:
            token_count = self.estimate_tokens(text)
            max_tokens = self.get_max_tokens("code")  # По умолчанию для кода
            report = {
                "token_count": token_count,
                "max_tokens": max_tokens,
                "remaining_tokens": max_tokens - token_count,
                "stop_sequences": self.get_stop_sequences()
            }
            return report
        except Exception as e:
            return {"error": str(e)}