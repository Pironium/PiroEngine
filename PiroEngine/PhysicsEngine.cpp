#include <iostream>
#include <vector>

// Определяем класс для объектов, подвергающихся физической симуляции
class PhysicsObject {
public:
    double mass;
    double velocity;

    PhysicsObject(double m, double v) : mass(m), velocity(v) {}
};

// Класс для физического движка
class PhysicsEngine {
public:
    std::vector<PhysicsObject> objects;

    // Метод для добавления объектов в симуляцию
    void AddObject(const PhysicsObject& obj) {
        objects.push_back(obj);
    }

    // Метод для выполнения физической симуляции
    void Simulate(double timeStep) {
        for (auto& obj : objects) {
            // Применяем ускорение (форс) с учетом массы
            double acceleration = 9.81; // Ускорение свободного падения (пример)
            obj.velocity += acceleration * timeStep;
        }
    }
};

int main() {
    // Создаем экземпляр физического движка
    PhysicsEngine physicsEngine;

    // Добавляем объекты в симуляцию
    PhysicsObject object1(5.0, 0.0);
    PhysicsObject object2(10.0, 0.0);
    physicsEngine.AddObject(object1);
    physicsEngine.AddObject(object2);

    // Запускаем симуляцию
    double timeStep = 0.01; // Временной шаг симуляции (пример)
    for (int i = 0; i < 100; ++i) {
        physicsEngine.Simulate(timeStep);
    }

    // Выводим результаты
    for (const auto& obj : physicsEngine.objects) {
        std::cout << "Object velocity: " << obj.velocity << std::endl;
    }

    return 0;
}
