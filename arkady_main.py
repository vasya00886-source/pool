#!/usr/bin/env python3

import sys
import os
from arkady_studio import ArkadyStudio
from arkady_router import ArkadyRouter
from arkady_memory import ArkadyMemory
from arkady_plugins import PluginManager
from arkady_security import SecurityManager

class ArkadyApp:
    def __init__(self):
        try:
            self.router = ArkadyRouter()
            self.memory = ArkadyMemory()
            self.plugins = PluginManager()
            self.security = SecurityManager()
            self.studio = ArkadyStudio()
        except Exception as e:
            print(f"Ошибка при инициализации: {e}", file=sys.stderr)

    def setup(self):
        try:
            # Инициализация всех слоёв
            pass
        except Exception as e:
            print(f"Ошибка при настройке: {e}", file=sys.stderr)

    def run(self):
        try:
            self.studio.run()
        except Exception as e:
            print(f"Ошибка при запуске: {e}", file=sys.stderr)

    def shutdown(self):
        try:
            self.memory.close()
            self.security.cleanup()
        except Exception as e:
            print(f"Ошибка при завершении: {e}", file=sys.stderr)