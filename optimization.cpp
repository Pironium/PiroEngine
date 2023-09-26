// optimization.cpp

#include <iostream>
#include <vector>

// Функция оптимизации для процессоров Intel
void optimizeForIntel() {
    std::cout << "Optimizing for Intel processors...\n";

    // Здесь добавим сложный код оптимизации для Intel
    // ...

    std::cout << "Optimization for Intel completed.\n";
}

// Функция оптимизации для процессоров AMD
void optimizeForAMD() {
    std::cout << "Optimizing for AMD processors...\n";

    // Здесь добавим сложный код оптимизации для AMD
    // ...

    std::cout << "Optimization for AMD completed.\n";
}

int main() {
    std::vector<int> processors;
    processors.push_back(1); // Intel
    processors.push_back(2); // AMD

    for (int processor : processors) {
        if (processor == 1) {
            optimizeForIntel();
        } else if (processor == 2) {
            optimizeForAMD();
        }
    }

    return 0;
}
