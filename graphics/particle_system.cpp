#include <iostream>
#include <vector>

class Particle {
public:
    float x, y, z;
    float velocityX, velocityY, velocityZ;
    float size;
    float lifespan;
    // Другие параметры частицы

    void update(float deltaTime) {
        // Логика обновления частицы
        x += velocityX * deltaTime;
        y += velocityY * deltaTime;
        z += velocityZ * deltaTime;
        lifespan -= deltaTime;
        // Другие обновления
    }

    bool isAlive() const {
        return lifespan > 0.0f;
    }
};

class ParticleSystem {
public:
    std::vector<Particle> particles;
    // Другие параметры системы частиц

    void emitParticle() {
        Particle particle;
        // Инициализация параметров частицы
        particles.push_back(particle);
    }

    void update(float deltaTime) {
        for (int i = 0; i < particles.size(); ++i) {
            particles[i].update(deltaTime);
            if (!particles[i].isAlive()) {
                particles.erase(particles.begin() + i);
                --i;
            }
        }
        // Другие обновления системы
    }
};

int main() {
    ParticleSystem particleSystem;
    // Инициализация системы частиц и другие настройки

    while (true) {
        // Главный цикл игры
        float deltaTime = 0.016f; // Примерное значение времени шага
        particleSystem.emitParticle();
        particleSystem.update(deltaTime);
        // Отрисовка частиц и другие действия
    }

    return 0;
}
