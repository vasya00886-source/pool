from rich.table import Table

class WorkflowDAG:
    def __init__(self):
        try:
            self.nodes = {}
            self.edges = []
        except Exception as e:
            print(f"Ошибка при инициализации WorkflowDAG: {e}")

    def add_node(self, name, task):
        try:
            if name in self.nodes:
                raise ValueError(f"Узел с именем '{name}' уже существует.")
            self.nodes[name] = task
        except Exception as e:
            print(f"Ошибка при добавлении узла: {e}")

    def add_edge(self, frm, to):
        try:
            if frm not in self.nodes or to not in self.nodes:
                raise ValueError("Один или оба из указанных узлов не существуют.")
            self.edges.append((frm, to))
        except Exception as e:
            print(f"Ошибка при добавлении ребра: {e}")

    def topo_sort(self):
        try:
            # Реализация топологической сортировки
            pass
        except Exception as e:
            print(f"Ошибка при топологической сортировке: {e}")

    def parallel_run(self):
        try:
            # Реализация параллельного выполнения узлов
            pass
        except Exception as e:
            print(f"Ошибка при параллельном выполнении: {e}")

    def visualize(self):
        try:
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Node", style="dim")
            table.add_column("Depends On")

            for node in self.nodes:
                dependencies = [frm for frm, to in self.edges if to == node]
                table.add_row(node, ", ".join(dependencies))

            print(table)
        except Exception as e:
            print(f"Ошибка при визуализации графа: {e}")

    def status(self):
        try:
            # Реализация метода для получения статусов узлов
            pass
        except Exception as e:
            print(f"Ошибка при получении статусов: {e}")