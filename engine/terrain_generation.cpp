#include <iostream>
#include <vector>
#include <random>

// Генерируем трехмерный ландшафт
std::vector<std::vector<std::vector<int>>> generateTerrain(int width, int height, int depth) {
    std::vector<std::vector<std::vector<int>>> terrain;
    terrain.resize(width, std::vector<std::vector<int>>(height, std::vector<int>(depth)));

    std::default_random_engine generator;
    std::uniform_int_distribution<int> distribution(0, 255);

    for (int x = 0; x < width; x++) {
        for (int y = 0; y < height; y++) {
            for (int z = 0; z < depth; z++) {
                terrain[x][y][z] = distribution(generator);
            }
        }
    }

    return terrain;
}

int main() {
    int width = 100;
    int height = 100;
    int depth = 50;

    std::vector<std::vector<std::vector<int>>> landscape = generateTerrain(width, height, depth);

    // Дополнительный код для работы с сгенерированным ландшафтом

    std::cout << "Трехмерный ландшафт успешно сгенерирован!" << std::endl;

    return 0;
}
