#include <stdlib.h>

// Function to allocate memory with error handling
void* allocate_memory(size_t size) {
    void* ptr = malloc(size);
    if (ptr == NULL) {
        perror("Memory allocation failed");
        exit(EXIT_FAILURE);
    }
    return ptr;
}

// Function to deallocate memory with error handling
void deallocate_memory(void* ptr) {
    if (ptr != NULL) {
        free(ptr);
    } else {
        perror("Attempted to deallocate a null pointer");
        exit(EXIT_FAILURE);
    }
}
