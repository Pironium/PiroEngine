#include <stdio.h>
#include <stdlib.h>

// PiroEngine Memory Protection Module

// Define a custom memory protection structure
typedef struct {
    unsigned char* memory_block;
    size_t size;
    int is_protected;
} MemoryProtection;

// Initialize a memory protection block
MemoryProtection* initializeMemoryProtection(size_t size) {
    MemoryProtection* protection = (MemoryProtection*)malloc(sizeof(MemoryProtection));
    if (protection == NULL) {
        fprintf(stderr, "Memory allocation error\n");
        exit(1);
    }

    protection->memory_block = (unsigned char*)malloc(size);
    if (protection->memory_block == NULL) {
        fprintf(stderr, "Memory allocation error\n");
        exit(1);
    }

    protection->size = size;
    protection->is_protected = 0; // Initially, memory is not protected

    // Initialize memory with zeros
    for (size_t i = 0; i < size; i++) {
        protection->memory_block[i] = 0;
    }

    return protection;
}

// Enable memory protection
void enableMemoryProtection(MemoryProtection* protection) {
    protection->is_protected = 1;
}

// Disable memory protection
void disableMemoryProtection(MemoryProtection* protection) {
    protection->is_protected = 0;
}

// Write data to protected memory
void writeProtectedMemory(MemoryProtection* protection, size_t offset, unsigned char* data, size_t data_size) {
    if (protection->is_protected) {
        fprintf(stderr, "Error: Attempt to write to protected memory\n");
        exit(1);
    }

    if (offset + data_size > protection->size) {
        fprintf(stderr, "Error: Memory write out of bounds\n");
        exit(1);
    }

    for (size_t i = 0; i < data_size; i++) {
        protection->memory_block[offset + i] = data[i];
    }
}

// Read data from protected memory
void readProtectedMemory(MemoryProtection* protection, size_t offset, unsigned char* data, size_t data_size) {
    if (offset + data_size > protection->size) {
        fprintf(stderr, "Error: Memory read out of bounds\n");
        exit(1);
    }

    for (size_t i = 0; i < data_size; i++) {
        data[i] = protection->memory_block[offset + i];
    }
}

// Deallocate memory protection structure
void cleanupMemoryProtection(MemoryProtection* protection) {
    free(protection->memory_block);
    free(protection);
}
