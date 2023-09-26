import threading

class ParallelTask:
    def __init__(self, function, args=()):
        self.function = function
        self.args = args

    def execute(self):
        thread = threading.Thread(target=self.function, args=self.args)
        thread.start()
        return thread

class ParallelTaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def wait_for_completion(self):
        for task in self.tasks:
            task.join()

# Пример использования:
def expensive_computation(task_id):
    print(f"Task {task_id}: Starting expensive computation...")
    # Здесь выполняется сложные вычисления
    print(f"Task {task_id}: Expensive computation completed!")

task_manager = ParallelTaskManager()

# Создаем и добавляем задачи в менеджер
for i in range(5):
    task = ParallelTask(expensive_computation, args=(i,))
    task_manager.add_task(task)

# Ждем завершения всех задач
task_manager.wait_for_completion()
print("All tasks have completed!")
