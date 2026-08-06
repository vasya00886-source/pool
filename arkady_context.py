from rich.panel import Panel
from rich.console import Console
from rich.table import Table

class ContextVisualizer:
    def __init__(self):
        pass

    def compress(self, messages):
        try:
            if len(messages) <= 5:
                return messages
            return messages[:2] + ['summary'] + messages[-3:]
        except Exception as e:
            print(f"Error in compress: {e}")
            return []

    def stats(self, before, after):
        try:
            tokens_saved = len(before) - len(after)
            ratio = len(after) / len(before) if len(before) > 0 else 1
            return {"tokens_saved": tokens_saved, "ratio": ratio}
        except Exception as e:
            print(f"Error in stats: {e}")
            return {}

    def visualize(self, before, after):
        try:
            stats = self.stats(before, after)
            console = Console()
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Metrics", justify="right")
            table.add_column("Before", justify="right")
            table.add_column("After", justify="right")

            table.add_row("Tokens", str(len(before)), str(len(after)))
            table.add_row("Tokens saved", str(stats.get("tokens_saved", 0)), "")
            table.add_row("Compression ratio", f"{stats.get('ratio', 1):.2f}", "")

            console.print(Panel(table, title="Context Compression Visualization"))
        except Exception as e:
            print(f"Error in visualize: {e}")

    def estimate(self, text):
        try:
            return len(text) // 4
        except Exception as e:
            print(f"Error in estimate: {e}")
            return 0

    def should_compress(self, messages):
        try:
            return len(messages) > 10
        except Exception as e:
            print(f"Error in should_compress: {e}")
            return False