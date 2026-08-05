from pathlib import Path

class PluginSandbox:
    def __init__(self):
        try:
            self.plugins_dir = Path('.arkady/plugins')
            if not self.plugins_dir.exists():
                self.plugins_dir.mkdir(parents=True)
            self.trusted = ['icon_generator', 'token_saver']
        except Exception as e:
            print(f"Error initializing PluginSandbox: {e}")

    def audit_plugin(self, code):
        DANGEROUS_PATTERNS = [
            r'os\.system',
            r'subprocess\.call\("cmd',
            r'eval\(input',
            r'exec\(input',
            r'__import__\("ctypes"',
            r'shutil.rmtree',
            r'open\("C:\\Windows'
        ]
        risks = [pattern for pattern in DANGEROUS_PATTERNS if re.search(pattern, code)]
        return len(risks) == 0, risks

    def uninstall(self, plugin_name):
        try:
            plugin_path = self.plugins_dir / f"{plugin_name}.py"
            if not plugin_path.exists():
                raise FileNotFoundError(f"Plugin '{plugin_name}' not found.")
            plugin_path.unlink()
            print(f"Plugin '{plugin_name}' uninstalled successfully.")
        except Exception as e:
            print(f"Error uninstalling plugin: {e}")