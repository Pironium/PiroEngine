#include <iostream>
#include <vector>
#include <cmath>

class WaterSurface {
public:
    WaterSurface(int width, int height, float damping) 
        : width_(width), height_(height), damping_(damping) {
        // Инициализация массивов высоты и скорости воды
        heightMap_.resize(width_ * height_);
        velocityMap_.resize(width_ * height_);
    }

    void Update(float deltaTime) {
        // Обновление высоты водной поверхности
        for (int x = 1; x < width_ - 1; ++x) {
            for (int y = 1; y < height_ - 1; ++y) {
                float height = heightMap_[x + y * width_];
                float prevHeight = height;
                float velocity = velocityMap_[x + y * width_];
                float neighborSum = heightMap_[(x - 1) + y * width_] +
                                    heightMap_[(x + 1) + y * width_] +
                                    heightMap_[x + (y - 1) * width_] +
                                    heightMap_[x + (y + 1) * width_];
                float newHeight = (neighborSum / 4.0f - height) * 2.0f - velocity;
                newHeight *= damping_;
                heightMap_[x + y * width_] = newHeight;
                velocityMap_[x + y * width_] = newHeight - prevHeight;
            }
        }
    }

    void Splash(int x, int y, float velocity) {
        if (x > 0 && x < width_ && y > 0 && y < height_) {
            velocityMap_[x + y * width_] += velocity;
        }
    }

private:
    int width_;
    int height_;
    float damping_;
    std::vector<float> heightMap_;
    std::vector<float> velocityMap_;
};

int main() {
    const int screenWidth = 800;
    const int screenHeight = 600;
    const float dampingFactor = 0.98f;

    WaterSurface water(screenWidth, screenHeight, dampingFactor);

    // Основной игровой цикл
    while (true) {
        // Обновление водной поверхности
        water.Update(0.016f); // Фиксированный шаг времени

        // Обработка пользовательского ввода (например, кликов мыши для создания волн)
        // ...

        // Отрисовка водной поверхности
        // ...

        // Обработка событий и другая логика игры
        // ...
    }

    return 0;
}
