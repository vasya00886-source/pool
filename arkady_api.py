import hashlib

class RuleEngine:
    def __init__(self, dev_key):
        self.dev_key = dev_key

    def integrity(self, data, expected_hash):
        try:
            actual_hash = hashlib.sha256(data).hexdigest()
            return actual_hash == expected_hash
        except Exception as e:
            print(f"Ошибка при проверке целостности: {e}")
            return False