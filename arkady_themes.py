class ThemeManager:
    def __init__(self):
        self.themes = {
            'dark': {'background': '#000', 'text': '#fff'},
            'light': {'background': '#fff', 'text': '#000'},
            'fire': {'background': '#ff4500', 'text': '#fff'}
        }
        self.current_theme = 'dark'

    def set_theme(self, theme):
        if theme in self.themes:
            self.current_theme = theme
        else:
            raise ValueError(f"Unsupported theme: {theme}")

    def get_themes(self):
        return list(self.themes.keys())

    def markdown_render(self, text):
        try:
            theme = self.themes[self.current_theme]
            return f"<div style='background-color: {theme['background']}; color: {theme['text']}'>{text}</div>"
        except KeyError as e:
            print(f"Error rendering text: {e}")
            return ""