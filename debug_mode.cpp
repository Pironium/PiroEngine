// debug_mode.cpp

#include <iostream>
#include <vector>
#include <thread>
#include <chrono>

class MemoryMonitor {
public:
    void StartMonitoring() {
        while (true) {
            std::this_thread::sleep_for(std::chrono::seconds(1));
            CheckMemoryUsage();
        }
    }

private:
    void CheckMemoryUsage() {
        // Simulate memory usage check
        std::vector<int> memoryConsumption(1000000, 0); // Using up memory

        // Print memory usage statistics
        std::cout << "Memory Usage - RSS: " << GetRSS() << " KB, Virtual: " << GetVirtualMemory() << " KB\n";
    }

    // Get Resident Set Size (RSS) memory usage
    long GetRSS() {
        // Simulate RSS memory retrieval
        return rand() % 1024 + 1024; // Random value between 1024 KB and 2047 KB
    }

    // Get virtual memory usage
    long GetVirtualMemory() {
        // Simulate virtual memory retrieval
        return rand() % 2048 + 2048; // Random value between 2048 KB and 4095 KB
    }
};

int main() {
    MemoryMonitor memoryMonitor;
    memoryMonitor.StartMonitoring();

    // Other engine initialization and game development code goes here

    return 0;
}
