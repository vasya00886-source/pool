class CronScheduler:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        try:
            self.tasks.append(task)
        except Exception as e:
            print(f"Ошибка при добавлении задачи: {e}")

    def list(self):
        try:
            for task in self.tasks:
                print(task)
        except Exception as e:
            print(f"Ошибка при выводе списка задач: {e}")

    def run(self, task):
        try:
            if callable(task):
                task()
            else:
                raise ValueError("Задача должна быть вызываемой")
        except Exception as e:
            print(f"Ошибка при выполнении задачи: {e}")

    def loop(self):
        try:
            while True:
                for task in self.tasks:
                    self.run(task)
        except KeyboardInterrupt:
            print("Цикл остановлен пользователем")
        except Exception as e:
            print(f"Ошибка в цикле: {e}")