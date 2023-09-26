#include <iostream>
#include <string>

// Функция оптимизации для процессоров Intel
void optimizeForIntel() {
    std::cout << "Optimizing for Intel processors..." << std::endl;
    // Ваш сложный и длинный код оптимизации для Intel здесь
}

// Функция оптимизации для процессоров AMD
void optimizeForAMD() {
    std::cout << "Optimizing for AMD processors..." << std::endl;
    // Ваш сложный и длинный код оптимизации для AMD здесь
}

int main() {
    std::string processorType;
    std::cout << "Enter the processor type (Intel/AMD): ";
    std::cin >> processorType;

    if (processorType == "Intel") {
        optimizeForIntel();
    } else if (processorType == "AMD") {
        optimizeForAMD();
    } else {
        std::cout << "Unknown processor type." << std::endl;
    }

    return 0;
}
