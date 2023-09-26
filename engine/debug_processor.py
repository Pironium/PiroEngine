import psutil  # Импортируем библиотеку для мониторинга процессора

class ProcessorDebugger:
    def __init__(self):
        self.cpu_percent = 0.0  # Изначально уровень использования процессора - 0%

    def update_cpu_load(self):
        # Получаем текущую нагрузку на процессор
        self.cpu_percent = psutil.cpu_percent(interval=1)

    def print_cpu_load(self):
        # Выводим информацию о нагрузке на процессор
        print(f"CPU Load: {self.cpu_percent}%")

# Пример использования
if __name__ == "__main__":
    processor_debugger = ProcessorDebugger()
    
    while True:
        processor_debugger.update_cpu_load()
        processor_debugger.print_cpu_load()
