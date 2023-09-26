#include <iostream>
#include <vector>
#include <random>

// Генерирует случайный ландшафт в 3D
std::vector<std::vector<std::vector<int>>> GenerateTerrain(int width, int length, int height) {
    std::vector<std::vector<std::vector<int>>> terrain;

    // Инициализируем генератор случайных чисел
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(0, 255);

    // Создаем 3D массив для хранения высот точек ландшафта
    for (int x = 0; x < width; ++x) {
        std::vector<std::vector<int>> row;
        for (int y = 0; y < length; ++y) {
            std::vector<int> column;
            for (int z = 0; z < height; ++z) {
                // Генерируем случайную высоту от 0 до 255
                int elevation = dis(gen);
                column.push_back(elevation);
            }
            row.push_back(column);
        }
        terrain.push_back(row);
    }

    return terrain;
}

int main() {
    int width = 100;
    int length = 100;
    int height = 50;

    std::vector<std::vector<std::vector<int>>> terrain = GenerateTerrain(width, length, height);

    // Выводим сгенерированный ландшафт
    for (int x = 0; x < width; ++x) {
        for (int y = 0; y < length; ++y) {
            for (int z = 0; z < height; ++z) {
                std::cout << "Terrain at (" << x << ", " << y << ", " << z << "): " << terrain[x][y][z] << std::endl;
            }
        }
    }

    return 0;
}
