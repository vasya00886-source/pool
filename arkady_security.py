import logging
from logging.handlers import RotatingFileHandler
import re

class SecurityManager:
    def __init__(self):
        self.api_key = None
        self.logger = self.setup_logging()

    def setup_logging(self):
        try:
            logger = logging.getLogger('SecurityManager')
            handler = RotatingFileHandler('security.log', maxBytes=1024*1024, backupCount=5)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
            return logger
        except Exception as e:
            self.logger.error(f"Failed to setup logging: {e}")
            return None

    def store_api_key(self, key):
        try:
            self.api_key = key
            self.logger.info("API key stored successfully.")
        except Exception as e:
            self.logger.error(f"Failed to store API key: {e}")

    def get_api_key(self):
        try:
            if self.api_key is None:
                raise ValueError("API key not set.")
            return self.api_key
        except Exception as e:
            self.logger.error(f"Failed to retrieve API key: {e}")
            return None

    def detect_secrets(self, text):
        try:
            # Пример регулярного выражения для обнаружения секретов
            secret_pattern = re.compile(r'api_key\s*=\s*[\'"]([^\']*)[\'"]')
            secrets = secret_pattern.findall(text)
            self.logger.info(f"Detected secrets: {secrets}")
            return secrets
        except Exception as e:
            self.logger.error(f"Failed to detect secrets: {e}")
            return []

    def sanitize_prompt(self, prompt):
        try:
            # Пример регулярного выражения для очистки входного текста
            sanitized = re.sub(r'\bapi_key\b', '[REDACTED]', prompt)
            self.logger.info(f"Sanitized prompt: {sanitized}")
            return sanitized
        except Exception as e:
            self.logger.error(f"Failed to sanitize prompt: {e}")
            return None