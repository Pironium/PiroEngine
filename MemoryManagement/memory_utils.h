#ifndef MEMORY_UTILS_H
#define MEMORY_UTILS_H

#include <stdlib.h>

void* PiroAllocateMemory(size_t size) {
    return malloc(size);
}

void PiroFreeMemory(void* ptr) {
    free(ptr);
}

void* PiroReallocateMemory(void* ptr, size_t size) {
    return realloc(ptr, size);
}

#endif // MEMORY_UTILS_H
