import os
from pathlib import Path
import json
import importlib
import shutil

class PluginManager:
    def __init__(self):
        try:
            self.plugins_dir = Path('.arkady/plugins')
            self.hooks = {}
        except Exception as e:
            print(f"Error initializing PluginManager: {e}")

    def register_hook(self, event, handler):
        try:
            if event not in self.hooks:
                self.hooks[event] = []
            self.hooks[event].append(handler)
        except Exception as e:
            print(f"Error registering hook: {e}")

    def trigger(self, event, context):
        try:
            if event in self.hooks:
                for handler in self.hooks[event]:
                    context = handler(context)
            return context
        except Exception as e:
            print(f"Error triggering event: {e}")
            return context

    def load_plugin(self, name):
        try:
            manifest_path = self.plugins_dir / name / 'plugin.json'
            if not manifest_path.exists():
                raise FileNotFoundError(f"Plugin manifest not found for {name}")
            with open(manifest_path, 'r', encoding='utf-8') as f:
                manifest = json.load(f)
            # Load the plugin module
            try:
                importlib.import_module(f'.{name}.plugin', package='arkady_plugins')
            except ImportError as e:
                print(f"Error importing plugin {name}: {e}")
                raise
            return manifest
        except Exception as e:
            print(f"Error loading plugin {name}: {e}")
            raise

    def list_plugins(self):
        try:
            plugins = [d.name for d in self.plugins_dir.iterdir() if d.is_dir()]
            return plugins
        except Exception as e:
            print(f"Error listing plugins: {e}")
            return []

    def install_plugin(self, source):
        try:
            # Implementation of install_plugin method
            pass
        except Exception as e:
            print(f"Error installing plugin from {source}: {e}")

    def uninstall_plugin(self, name):
        try:
            plugin_path = self.plugins_dir / name
            if not plugin_path.exists():
                raise FileNotFoundError(f"Plugin directory not found for {name}")
            if not plugin_path.is_dir():
                raise NotADirectoryError(f"The path for {name} is not a directory")
            shutil.rmtree(plugin_path)
        except Exception as e:
            print(f"Error uninstalling plugin {name}: {e}")