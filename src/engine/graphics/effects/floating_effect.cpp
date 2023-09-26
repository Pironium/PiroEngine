#include <iostream>
#include <vector>
#include <cmath>

class FloatingEffect {
public:
    FloatingEffect(float amplitude, float frequency) : amplitude_(amplitude), frequency_(frequency) {}

    void ApplyFloatingEffect(std::vector<float>& positions, float deltaTime) {
        float time = static_cast<float>(clock()) / CLOCKS_PER_SEC;
        float displacement = amplitude_ * sin(2.0f * M_PI * frequency_ * time);

        for (size_t i = 1; i < positions.size(); i += 3) {
            positions[i] += displacement * deltaTime;
        }
    }

private:
    float amplitude_;
    float frequency_;
};

int main() {
    // Пример использования эффекта "плавания"
    float amplitude = 0.5f;   // Амплитуда плавания
    float frequency = 1.0f;  // Частота плавания

    FloatingEffect floatingEffect(amplitude, frequency);

    // Здесь вы имеете позиции объектов в 3D пространстве (x, y, z координаты)
    std::vector<float> objectPositions = {
        0.0f, 1.0f, 0.0f,   // Первый объект
        2.0f, 0.0f, -1.0f,  // Второй объект
        // ... Добавьте позиции других объектов здесь ...
    };

    // Симулируем плавание объектов с использованием эффекта
    float deltaTime = 0.016f;  // Примерное время между кадрами (в секундах)
    floatingEffect.ApplyFloatingEffect(objectPositions, deltaTime);

    // Теперь позиции объектов обновлены с учетом эффекта "плавания"
    std::cout << "Floating effect applied successfully!" << std::endl;

    return 0;
}
