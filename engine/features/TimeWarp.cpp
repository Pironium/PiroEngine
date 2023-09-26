#include <iostream>
#include <chrono>
#include <thread>

class TimeWarp {
public:
    TimeWarp(float timeScale) : timeScale_(timeScale) {}

    void SetTimeScale(float timeScale) {
        timeScale_ = timeScale;
    }

    void Update() {
        std::chrono::duration<float> deltaTime = std::chrono::high_resolution_clock::now() - lastFrameTime_;
        lastFrameTime_ = std::chrono::high_resolution_clock::now();

        deltaTime *= timeScale_;

        // Применяем TimeWarp к игре
        // ...

        std::this_thread::sleep_for(deltaTime); // Симуляция прошедшего времени
    }

private:
    float timeScale_;
    std::chrono::time_point<std::chrono::high_resolution_clock> lastFrameTime_;
};

int main() {
    TimeWarp timeWarp(1.0f); // Инициализация с нормальным временем

    while (true) {
        // Обновление игры с учетом TimeWarp
        timeWarp.Update();
    }

    return 0;
}
