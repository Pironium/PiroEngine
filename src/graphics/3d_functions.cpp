#include <iostream>
#include <cmath>
#include <vector>

class PiroEngine {
public:
    PiroEngine() {
        std::cout << "Initializing PiroEngine..." << std::endl;
    }

    ~PiroEngine() {
        std::cout << "Shutting down PiroEngine..." << std::endl;
    }

    // Уникальная 3D функция: Генерация сферической гравитации
    std::vector<float> generateSphericalGravity(int numParticles, float radius) {
        std::vector<float> gravityField;
        for (int i = 0; i < numParticles; ++i) {
            float theta = static_cast<float>(rand()) / static_cast<float>(RAND_MAX) * M_PI;
            float phi = static_cast<float>(rand()) / static_cast<float>(RAND_MAX) * (2 * M_PI);
            float x = radius * sin(theta) * cos(phi);
            float y = radius * sin(theta) * sin(phi);
            float z = radius * cos(theta);
            gravityField.push_back(x);
            gravityField.push_back(y);
            gravityField.push_back(z);
        }
        return gravityField;
    }
};

int main() {
    PiroEngine engine;
    std::vector<float> gravityField = engine.generateSphericalGravity(1000, 10.0);

    std::cout << "Generated gravity field with " << gravityField.size() / 3 << " particles." << std::endl;

    return 0;
}
