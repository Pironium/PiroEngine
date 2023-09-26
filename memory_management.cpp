// memory_management.cpp

#include <iostream>
#include <vector>
#include <algorithm>

class MemoryManager {
public:
    MemoryManager(int maxMemorySize) : maxMemorySize(maxMemorySize) {
        memory.reserve(maxMemorySize);
    }

    void allocateMemory(int size) {
        if (size <= 0) {
            std::cerr << "Invalid memory allocation size!" << std::endl;
            return;
        }

        if (availableMemory() < size) {
            std::cerr << "Memory allocation failed. Not enough memory available." << std::endl;
            return;
        }

        // Find a suitable block of memory or create a new one
        auto it = std::find_if(memory.begin(), memory.end(), [size](const MemoryBlock& block) {
            return !block.allocated && block.size >= size;
        });

        if (it != memory.end()) {
            // Allocate memory from an existing block
            allocateFromBlock(*it, size);
        } else {
            // Create a new memory block
            createMemoryBlock(size);
        }
    }

    void deallocateMemory(int address) {
        auto it = std::find_if(memory.begin(), memory.end(), [address](const MemoryBlock& block) {
            return block.startAddress == address && block.allocated;
        });

        if (it != memory.end()) {
            it->allocated = false;
            std::cout << "Memory deallocated successfully." << std::endl;
        } else {
            std::cerr << "Memory deallocation failed. Address not found or memory is not allocated." << std::endl;
        }
    }

    int availableMemory() const {
        int usedMemory = 0;
        for (const auto& block : memory) {
            if (block.allocated) {
                usedMemory += block.size;
            }
        }
        return maxMemorySize - usedMemory;
    }

private:
    struct MemoryBlock {
        int startAddress;
        int size;
        bool allocated;
    };

    int maxMemorySize;
    std::vector<MemoryBlock> memory;

    void allocateFromBlock(MemoryBlock& block, int size) {
        if (block.size == size) {
            block.allocated = true;
            std::cout << "Memory allocated successfully." << std::endl;
        } else {
            // Split the block into two parts (allocated and unallocated)
            MemoryBlock newBlock{block.startAddress + size, block.size - size, false};
            block.size = size;
            block.allocated = true;
            memory.insert(std::next(memory.begin(), std::distance(memory.begin(), it) + 1), newBlock);
            std::cout << "Memory allocated successfully." << std::endl;
        }
    }

    void createMemoryBlock(int size) {
        if (availableMemory() >= size) {
            // Find the first available address for the new block
            int address = 0;
            for (const auto& block : memory) {
                if (block.startAddress - address >= size) {
                    break;
                }
                address = block.startAddress + block.size;
            }

            MemoryBlock newBlock{address, size, true};
            memory.push_back(newBlock);
            std::cout << "Memory allocated successfully." << std::endl;
        } else {
            std::cerr << "Memory allocation failed. Not enough memory available." << std::endl;
        }
    }
};

int main() {
    // Example usage of the MemoryManager
    MemoryManager memoryManager(1024); // Initialize with 1024 bytes of memory

    memoryManager.allocateMemory(256); // Allocate 256 bytes
    memoryManager.allocateMemory(512); // Allocate 512 bytes
    memoryManager.deallocateMemory(256); // Deallocate 256 bytes
    memoryManager.allocateMemory(128); // Allocate 128 bytes

    return 0;
}
