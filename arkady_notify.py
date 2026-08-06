import ctypes

class Notifier:
    def notify(self, title, message):
        try:
            ctypes.windll.user32.MessageBoxW(0, message, title, 1)
        except Exception as e:
            print(f"Ошибка при отображении уведомления: {e}")