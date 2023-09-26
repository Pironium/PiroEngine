#include <iostream>
#include <vector>
#include <string>

// Функция для оптимизации графики под NVIDIA
void OptimizeForNvidia(std::vector<std::string>& gameAssets) {
    std::cout << "Optimizing graphics for NVIDIA...\n";
    // Здесь добавьте код для оптимизации текстур, шейдеров и других ресурсов для NVIDIA
    for (const std::string& asset : gameAssets) {
        // Оптимизировать ресурс для NVIDIA
        // Например, сжатие текстур или оптимизация шейдеров
        std::cout << "Optimizing " << asset << " for NVIDIA...\n";
    }
}

// Функция для оптимизации графики под AMD
void OptimizeForAmd(std::vector<std::string>& gameAssets) {
    std::cout << "Optimizing graphics for AMD...\n";
    // Здесь добавьте код для оптимизации текстур, шейдеров и других ресурсов для AMD
    for (const std::string& asset : gameAssets) {
        // Оптимизировать ресурс для AMD
        // Например, оптимизация для архитектуры AMD
        std::cout << "Optimizing " << asset << " for AMD...\n";
    }
}

int main() {
    // Список игровых ресурсов, которые нужно оптимизировать
    std::vector<std::string> gameAssets = {"texture1.png", "shader.vs", "model.obj"};

    // Вызываем функции оптимизации для NVIDIA и AMD
    OptimizeForNvidia(gameAssets);
    OptimizeForAmd(gameAssets);

    return 0;
}
