#include <iostream>
#include <vector>
#include "piro_shader.h"

// Вспомогательная функция для оптимизации кода под Nvidia
void OptimizeForNvidia(const PiroShader& shader) {
    // Ваш код оптимизации для Nvidia
    std::cout << "Optimizing for Nvidia..." << std::endl;
}

// Вспомогательная функция для оптимизации кода под AMD
void OptimizeForAmd(const PiroShader& shader) {
    // Ваш код оптимизации для AMD
    std::cout << "Optimizing for AMD..." << std::endl;
}

// Новая функция для оптимизации под обе видеокарты
void OptimizeForBoth(const PiroShader& shader) {
    OptimizeForNvidia(shader);
    OptimizeForAmd(shader);
}

int main() {
    PiroShader shader("example_shader.pis");

    // Вызываем новую функцию для оптимизации под Nvidia и AMD
    OptimizeForBoth(shader);

    return 0;
}
