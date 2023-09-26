#include <stdlib.h>

// Структура для представления блока памяти
typedef struct MemoryBlock {
    void* address;          // Указатель на начало блока
    size_t size;            // Размер блока
    struct MemoryBlock* next; // Следующий блок в цепочке
} MemoryBlock;

// Глобальный указатель на начало списка блоков памяти
static MemoryBlock* memoryList = NULL;

// Функция для выделения памяти
void* allocateMemory(size_t size) {
    // Используем стандартную функцию malloc для выделения памяти
    void* ptr = malloc(size);
    
    // Создаем новый блок памяти и добавляем его в список
    MemoryBlock* block = (MemoryBlock*)malloc(sizeof(MemoryBlock));
    block->address = ptr;
    block->size = size;
    block->next = memoryList;
    memoryList = block;
    
    return ptr;
}

// Функция для освобождения памяти
void freeMemory(void* ptr) {
    MemoryBlock* current = memoryList;
    MemoryBlock* previous = NULL;
    
    // Ищем блок памяти, который нужно освободить
    while (current) {
        if (current->address == ptr) {
            // Найден блок, освобождаем его
            free(ptr);
            
            // Удаляем блок из списка
            if (previous) {
                previous->next = current->next;
            } else {
                memoryList = current->next;
            }
            
            free(current);
            break;
        }
        
        previous = current;
        current = current->next;
    }
}
