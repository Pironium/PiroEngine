import psutil
import threading
import time

class MemoryMonitoring:
    def __init__(self):
        self.memory_usage = 0
        self.monitoring_interval = 5  # Adjust the interval as needed
        self.monitoring_thread = threading.Thread(target=self.monitor_memory_usage)
        self.monitoring_thread.daemon = True
        self.monitoring_thread.start()

    def monitor_memory_usage(self):
        while True:
            memory_info = psutil.virtual_memory()
            self.memory_usage = memory_info.percent
            time.sleep(self.monitoring_interval)

    def get_memory_usage(self):
        return self.memory_usage

if __name__ == "__main__":
    memory_monitor = MemoryMonitoring()

    while True:
        current_memory_usage = memory_monitor.get_memory_usage()
        print(f"Current memory usage: {current_memory_usage}%")
        # Add more debugging or logging logic here as needed
        time.sleep(10)  # Adjust the interval for checking memory usage
