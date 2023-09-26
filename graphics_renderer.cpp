#include <iostream>
#include <vector>
#include <cmath>

class GraphicsRenderer {
public:
    GraphicsRenderer() {
        // Инициализация графического движка
        std::cout << "Initializing PiroEngine Graphics Renderer..." << std::endl;
    }

    // Уникальная функция для 3D движка: создание сферы
    void createSphere(float radius, int segments) {
        std::vector<float> sphereVertices;
        std::vector<float> sphereNormals;
        std::vector<int> sphereIndices;

        // Генерация вершин, нормалей и индексов для сферы
        for (int i = 0; i <= segments; ++i) {
            float phi = 2.0f * M_PI * float(i) / float(segments);
            for (int j = 0; j <= segments; ++j) {
                float theta = M_PI * float(j) / float(segments);
                float x = radius * std::sin(theta) * std::cos(phi);
                float y = radius * std::sin(theta) * std::sin(phi);
                float z = radius * std::cos(theta);

                sphereVertices.push_back(x);
                sphereVertices.push_back(y);
                sphereVertices.push_back(z);

                sphereNormals.push_back(x / radius);
                sphereNormals.push_back(y / radius);
                sphereNormals.push_back(z / radius);
            }
        }

        // Генерация индексов для отрисовки сферы
        for (int i = 0; i < segments; ++i) {
            for (int j = 0; j < segments; ++j) {
                int p0 = i * (segments + 1) + j;
                int p1 = p0 + 1;
                int p2 = (i + 1) * (segments + 1) + j;
                int p3 = p2 + 1;

                // Первый треугольник
                sphereIndices.push_back(p0);
                sphereIndices.push_back(p2);
                sphereIndices.push_back(p1);

                // Второй треугольник
                sphereIndices.push_back(p1);
                sphereIndices.push_back(p2);
                sphereIndices.push_back(p3);
            }
        }

        // Отправка данных в графический движок
        std::cout << "Creating a 3D sphere with radius " << radius << " and " << segments << " segments." << std::endl;
        // Здесь было бы подключение к реальному графическому движку.
    }
};

int main() {
    GraphicsRenderer renderer;
    renderer.createSphere(1.0f, 32);

    return 0;
}
