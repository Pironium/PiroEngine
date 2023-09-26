# Debug Utility Functions for PiroEngine

import psutil
import time

def track_memory_usage():
    """
    Track memory usage of the PiroEngine process.
    """
    process = psutil.Process()
    while True:
        memory_info = process.memory_info()
        print(f"Memory Usage: {memory_info.rss / (1024 * 1024):.2f} MB")
        time.sleep(5)

def track_cpu_usage():
    """
    Track CPU usage of the PiroEngine process.
    """
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        print(f"CPU Usage: {cpu_percent}%")
        time.sleep(5)

def track_gpu_usage():
    """
    Track GPU usage using a custom GPU monitoring library (not shown here).
    """
    while True:
        gpu_percent = monitor_gpu_usage()
        print(f"GPU Usage: {gpu_percent}%")
        time.sleep(5)

def debug_mode_main():
    """
    Entry point for the debug mode of PiroEngine.
    """
    print("Debug Mode for PiroEngine - Monitoring Resources")
    print("Press Ctrl+C to exit.")
    
    # Start tracking memory, CPU, and GPU usage concurrently
    memory_thread = Thread(target=track_memory_usage)
    cpu_thread = Thread(target=track_cpu_usage)
    gpu_thread = Thread(target=track_gpu_usage)
    
    memory_thread.start()
    cpu_thread.start()
    gpu_thread.start()
    
    # Wait for threads to finish (will never happen in this example)
    memory_thread.join()
    cpu_thread.join()
    gpu_thread.join()

if __name__ == "__main__":
    debug_mode_main()
