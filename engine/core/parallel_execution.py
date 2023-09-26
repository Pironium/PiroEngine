import threading

class ParallelExecutor:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def execute_tasks(self):
        threads = []
        for task in self.tasks:
            thread = threading.Thread(target=task)
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

# Пример использования:
if __name__ == "__main__":
    def task1():
        print("Task 1 is running")

    def task2():
        print("Task 2 is running")

    def task3():
        print("Task 3 is running")

    executor = ParallelExecutor()
    executor.add_task(task1)
    executor.add_task(task2)
    executor.add_task(task3)
    executor.execute_tasks()
