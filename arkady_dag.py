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
