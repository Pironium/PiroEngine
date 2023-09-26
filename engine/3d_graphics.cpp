#include <iostream>
#include <vector>
#include <cmath>

class PiroEngine {
public:
    PiroEngine() {
        std::cout << "PiroEngine initialized!" << std::endl;
    }

    // Уникальная функция: Создание 3D модели с использованием сплайнов
    void create3DModelWithSplines(std::vector<float> controlPoints) {
        // Ваш сложный код для создания 3D модели с использованием сплайнов здесь
        // ...
        std::cout << "3D модель создана с использованием сплайнов!" << std::endl;
    }
};

int main() {
    PiroEngine engine;
    std::vector<float> controlPoints = {0.0f, 0.0f, 0.0f, 1.0f, 1.0f, 1.0f, 2.0f, 2.0f, 2.0f};
    engine.create3DModelWithSplines(controlPoints);
    return 0;
}
