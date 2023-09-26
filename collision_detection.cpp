#include <iostream>
#include <vector>
#include <cmath>

// Определение класса для представления объекта в пространстве
class GameObject {
public:
    float x, y, z;
    float width, height, depth;
};

// Функция для определения коллизии между двумя объектами
bool CheckCollision(const GameObject& obj1, const GameObject& obj2) {
    // Вычисляем расстояние между центрами объектов
    float dx = obj1.x - obj2.x;
    float dy = obj1.y - obj2.y;
    float dz = obj1.z - obj2.z;

    // Вычисляем минимальное расстояние между объектами по каждой оси
    float minDistanceX = (obj1.width + obj2.width) / 2;
    float minDistanceY = (obj1.height + obj2.height) / 2;
    float minDistanceZ = (obj1.depth + obj2.depth) / 2;

    // Проверяем коллизию по каждой оси
    bool collisionX = std::abs(dx) < minDistanceX;
    bool collisionY = std::abs(dy) < minDistanceY;
    bool collisionZ = std::abs(dz) < minDistanceZ;

    // Объекты сталкиваются, если коллизия произошла по всем осям
    return collisionX && collisionY && collisionZ;
}

int main() {
    // Создаем два объекта
    GameObject obj1, obj2;
    obj1.x = 0.0f;
    obj1.y = 0.0f;
    obj1.z = 0.0f;
    obj1.width = 2.0f;
    obj1.height = 2.0f;
    obj1.depth = 2.0f;

    obj2.x = 1.0f;
    obj2.y = 1.0f;
    obj2.z = 1.0f;
    obj2.width = 2.0f;
    obj2.height = 2.0f;
    obj2.depth = 2.0f;

    // Проверяем коллизию между объектами
    if (CheckCollision(obj1, obj2)) {
        std::cout << "Collision detected!" << std::endl;
    } else {
        std::cout << "No collision." << std::endl;
    }

    return 0;
}
