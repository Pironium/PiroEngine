#include <iostream>
#include <vector>
#include <random>

class PiroEngine {
public:
    PiroEngine() {
        // Конструктор движка
    }

    // Новая функция для генерации случайных 3D объектов
    std::vector<std::string> generateRandom3DObjects(int numObjects) {
        std::vector<std::string> objects;

        for (int i = 0; i < numObjects; ++i) {
            std::string object;
            int complexity = getRandomComplexity(); // Генерация сложности объекта
            object = generate3DObject(complexity);
            objects.push_back(object);
        }

        return objects;
    }

private:
    // Генерация случайной сложности объекта (пример)
    int getRandomComplexity() {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<> dis(1, 5);
        return dis(gen);
    }

    // Генерация 3D объекта на основе сложности (пример)
    std::string generate3DObject(int complexity) {
        std::string object;
        for (int i = 0; i < complexity; ++i) {
            object += "Vertex " + std::to_string(i) + ", ";
        }
        return object;
    }
};

int main() {
    PiroEngine engine;
    std::vector<std::string> randomObjects = engine.generateRandom3DObjects(10);

    for (const auto& obj : randomObjects) {
        std::cout << "Generated Object: " << obj << std::endl;
    }

    return 0;
}
