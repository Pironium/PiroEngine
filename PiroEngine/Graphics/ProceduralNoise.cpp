#include <iostream>
#include <cmath>
#include <vector>

// Генерация процедурного шума с использованием Perlin Noise
std::vector<std::vector<float>> GenerateProceduralNoise(int width, int height, float scale, int octaves, float persistence) {
    std::vector<std::vector<float>> noiseMap(height, std::vector<float>(width, 0.0f));
    float maxNoiseValue = std::numeric_limits<float>::min();
    float minNoiseValue = std::numeric_limits<float>::max();

    for (int y = 0; y < height; ++y) {
        for (int x = 0; x < width; ++x) {
            float amplitude = 1.0f;
            float frequency = 1.0f;
            float noiseValue = 0.0f;

            for (int i = 0; i < octaves; ++i) {
                float sampleX = x / scale * frequency;
                float sampleY = y / scale * frequency;
                float perlinValue = /* Implement Perlin Noise function here */;
                
                noiseValue += perlinValue * amplitude;
                maxNoiseValue = std::max(maxNoiseValue, noiseValue);
                minNoiseValue = std::min(minNoiseValue, noiseValue);

                amplitude *= persistence;
                frequency *= 2.0f;
            }

            noiseMap[y][x] = noiseValue;
        }
    }

    // Нормализация значений шума
    for (int y = 0; y < height; ++y) {
        for (int x = 0; x < width; ++x) {
            noiseMap[y][x] = (noiseMap[y][x] - minNoiseValue) / (maxNoiseValue - minNoiseValue);
        }
    }

    return noiseMap;
}

int main() {
    int width = 512;
    int height = 512;
    float scale = 0.1f;
    int octaves = 6;
    float persistence = 0.5f;

    std::vector<std::vector<float>> noiseMap = GenerateProceduralNoise(width, height, scale, octaves, persistence);

    // Вывод значений шума или сохранение в текстурный файл
    // ...

    return 0;
}
