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
                    ratio = len(after) / len(before) if len(before) > 0 else 0
                    return {'tokens_saved': tokens_saved, 'ratio': ratio}
                except Exception as e:
                    print(f"Error in stats: {e}")
                    return {}

            def visualize(self, before, after):
                try:
                    from rich import print
                    from rich.panel import Panel
                    from rich.progress_bar import ProgressBar

                    panel = Panel(
                        f"Before: {len(before)}\nAfter: {len(after)}",
                        title="Compression Visualization"
                    )
                    bar = ProgressBar(total=len(before), completed=len(after))
                    print(panel)
                    print(bar)
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