#include <iostream>
#include <vector>
#include <random>

// Define a class for terrain generation
class TerrainGenerator {
public:
    TerrainGenerator(int width, int length, int seed) 
        : width_(width), length_(length), seed_(seed) {}

    // Generate a random terrain heightmap
    std::vector<std::vector<float>> GenerateTerrain() {
        std::vector<std::vector<float>> terrain;
        terrain.resize(width_, std::vector<float>(length_, 0.0f));

        std::default_random_engine rng(seed_);
        std::uniform_real_distribution<float> height_distribution(0.0f, 1.0f);

        for (int x = 0; x < width_; ++x) {
            for (int z = 0; z < length_; ++z) {
                terrain[x][z] = height_distribution(rng);
            }
        }

        return terrain;
    }

private:
    int width_;
    int length_;
    int seed_;
};

int main() {
    int width = 256;
    int length = 256;
    int seed = 12345;

    TerrainGenerator terrain_generator(width, length, seed);
    std::vector<std::vector<float>> terrain = terrain_generator.GenerateTerrain();

    // Output the generated terrain data (for testing)
    for (int x = 0; x < width; ++x) {
        for (int z = 0; z < length; ++z) {
            std::cout << terrain[x][z] << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}
