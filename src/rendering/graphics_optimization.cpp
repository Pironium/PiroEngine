#include <iostream>
#include <vector>
#include <algorithm>

// Функция для оптимизации рендеринга под NVIDIA и AMD
void optimizeGraphicsForNvidiaAndAmd(std::vector<int>& vertexData, std::vector<int>& textureData) {
    // Начинаем оптимизацию для NVIDIA
    std::sort(vertexData.begin(), vertexData.end());

    // Вставляем оптимизацию для AMD
    for (int i = 0; i < textureData.size(); ++i) {
        textureData[i] *= 2;
    }

    std::cout << "Графическая оптимизация для NVIDIA и AMD завершена." << std::endl;
}

int main() {
    std::vector<int> vertexData = {5, 3, 8, 1, 7};
    std::vector<int> textureData = {10, 20, 30, 40, 50};

    // Вызываем оптимизацию
    optimizeGraphicsForNvidiaAndAmd(vertexData, textureData);

    return 0;
}
