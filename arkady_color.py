class ColorPicker:
    def __init__(self):
        self.colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#00FFFF", "#FF00FF", "#FFFFFF", "#000000", "#800000", "#008000", "#000080", "#808000", "#008080", "#800080", "#C0C0C0"]

    def pick(self):
        try:
            # Реализация выбора цвета и возврата шестнадцатеричного кода
            return self.colors[0]  # Примерный возвращаемый результат
        except Exception as e:
            print(f"Ошибка при выборе цвета: {e}")
            return None

    def palette(self):
        try:
            return self.colors
        except Exception as e:
            print(f"Ошибка при получении палитры: {e}")
            return []