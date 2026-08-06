from rich import Panel

class HotkeyManager:
    def __init__(self):
        self.bindings = {
            'F1': 'help',
            'F5': 'run',
            'Ctrl-S': 'save',
            'Ctrl-K': 'scroll_up',
            'Ctrl-J': 'scroll_down',
            'Ctrl-N': 'new_session',
            'Ctrl-L': 'clear',
            'Ctrl-T': 'token_dashboard',
            'Ctrl-P': 'privacy_toggle',
            'Esc': 'back'
        }

    def handle(self, key):
        try:
            action = self.bindings.get(key)
            if action == 'help':
                self.show_help()
            elif action == 'token_dashboard':
                self.token_dashboard(stats)
            # Добавьте другие действия здесь
        except Exception as e:
            print(f"Error handling key {key}: {e}")

    def show_help(self):
        try:
            from rich.table import Table
            table = Table(title="Hotkeys")
            table.add_column("Key", style="bold magenta")
            table.add_column("Action", style="bold green")
            for key, action in self.bindings.items():
                table.add_row(key, action)
            print(table)
        except Exception as e:
            print(f"Error showing help: {e}")

    def privacy_toggle(self):
        try:
            # Реализация переключения между локальным и облачным режимом
            pass
        except Exception as e:
            print(f"Error toggling privacy: {e}")

    def token_dashboard(self, stats):
        try:
            panel = Panel(stats, title="Token Dashboard")
            print(panel)
        except Exception as e:
            print(f"Error displaying token dashboard: {e}")