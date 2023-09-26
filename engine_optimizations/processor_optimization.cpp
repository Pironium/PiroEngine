#include <iostream>
#include <cstring>

// Функция оптимизации для процессоров Intel
void optimizeForIntel() {
    std::cout << "Optimizing for Intel processors...\n";
    // Вставьте здесь код оптимизации для процессоров Intel
}

// Функция оптимизации для процессоров AMD
void optimizeForAMD() {
    std::cout << "Optimizing for AMD processors...\n";
    // Вставьте здесь код оптимизации для процессоров AMD
}

int main() {
    // Определяем тип процессора
    char processorType[20];
    std::cout << "Enter processor type (Intel/AMD): ";
    std::cin >> processorType;

    if (strcmp(processorType, "Intel") == 0) {
        optimizeForIntel();
    } else if (strcmp(processorType, "AMD") == 0) {
        optimizeForAMD();
    } else {
        std::cout << "Unsupported processor type.\n";
    }

    return 0;
}
