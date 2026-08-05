from rich.console import Console

class UIComponents:
    def __init__(self):
        self.console = Console()

    def privacy_indicator(self, provider):
        try:
            if provider == "local":
                emoji = "🟢"
            elif provider == "cloud":
                emoji = "🔴"
            else:
                emoji = "❓"
            
            self.console.print(f"Privacy Status: {emoji}")
        except Exception as e:
            self.console.print(f"Error displaying privacy indicator: {e}")