#include <iostream>
#include <vector>
#include <thread>
#include <chrono>

class MemoryMonitor {
public:
    MemoryMonitor() {}

    // Function to simulate memory usage tracking
    void TrackMemoryUsage() {
        while (true) {
            // Simulate memory usage
            std::vector<char> memoryBlock(1024 * 1024); // Allocate 1MB of memory
            memoryBlocks.push_back(memoryBlock);

            // Print current memory usage
            std::cout << "Memory Usage: " << memoryBlocks.size() << " MB\n";

            std::this_thread::sleep_for(std::chrono::seconds(1)); // Sleep for 1 second
        }
    }

private:
    std::vector<std::vector<char>> memoryBlocks;
};

int main() {
    MemoryMonitor memoryMonitor;

    // Start memory monitoring in a separate thread
    std::thread memoryTrackingThread(&MemoryMonitor::TrackMemoryUsage, &memoryMonitor);

    // Allow the monitoring thread to run for some time
    std::this_thread::sleep_for(std::chrono::minutes(5));

    // Stop the memory monitoring thread (in a real implementation, you would handle thread termination properly)
    memoryTrackingThread.join();

    return 0;
}
