#include <iostream>
#include <vector>
#include <random>

// Define a function to generate terrain for our game world
std::vector<std::vector<float>> generateTerrain(int width, int height) {
    std::vector<std::vector<float>> terrainMap(width, std::vector<float>(height, 0.0f));
    
    // Initialize a random number generator
    std::mt19937 rng(std::random_device{}());
    std::uniform_real_distribution<float> distribution(-1.0f, 1.0f);
    
    // Generate terrain heights
    for (int x = 0; x < width; ++x) {
        for (int y = 0; y < height; ++y) {
            terrainMap[x][y] = distribution(rng);
        }
    }
    
    // Apply smoothing or other terrain algorithms here if needed
    
    return terrainMap;
}

int main() {
    // Example usage of the generateTerrain function
    int mapWidth = 256;
    int mapHeight = 256;
    
    std::vector<std::vector<float>> gameTerrain = generateTerrain(mapWidth, mapHeight);
    
    // Output terrain data or use it for game rendering
    for (int x = 0; x < mapWidth; ++x) {
        for (int y = 0; y < mapHeight; ++y) {
            std::cout << gameTerrain[x][y] << " ";
        }
        std::cout << std::endl;
    }
    
    return 0;
}
