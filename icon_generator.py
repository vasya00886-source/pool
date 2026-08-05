from PIL import Image, ImageDraw, ImageFont

class IconGenerator:
    def __init__(self):
        self.size = 256

    def generate(self):
        # Создание черного фона
        image = Image.new('RGB', (self.size, self.size), 'black')
        draw = ImageDraw.Draw(image)

        # Определяем шрифты
        font_large = self.get_font(80)
        font_small = self.get_font(40)

        # Рисуем заглавную букву A с оранжево-огненным градиентом
        gradient_size = 128
        for i in range(gradient_size):
            color = (255 - int(i * 2), 165, 0)  # Оранжевый градиент к черному
            draw.text((self.size // 2 - gradient_size // 2 + i, self.size // 4),
                      'A', font=font_large, fill=color)

        # Рисуем букву a рядом
        draw.text((self.size // 2 + gradient_size // 2, self.size // 4),
                  'a', font=font_small, fill=(255, 165, 0))

        # Рисуем букву i ниже
        draw.text((self.size // 2 - gradient_size // 2, self.size // 2),
                  'i', font=font_large, fill=(255, 165, 0))

        # Рисуем текст "Studio" внизу
        draw.text((self.size // 2 - gradient_size // 4, self.size * 3 // 4),
                  'Studio', font=font_small, fill=(255, 165, 0))

        return image

    def save_ico(self, path):
        try:
            image = self.generate()
            image.save(path, format='ICO')
        except Exception as e:
            print(f"Ошибка при сохранении файла .ico: {e}")

    def save_png(self, path):
        try:
            image = self.generate()
            image.save(path, format='PNG')
        except Exception as e:
            print(f"Ошибка при сохранении файла .png: {e}")

    def get_font(self, size):
        return ImageFont.truetype("arial.ttf", size)

# Пример использования
if __name__ == "__main__":
    generator = IconGenerator()
    generator.save_ico("icon.ico")
    generator.save_png("icon.png")