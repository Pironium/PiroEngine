#include <iostream>
#include <vector>
#include <random>

class TerrainGenerator {
public:
    TerrainGenerator(int width, int height, int depth) : width_(width), height_(height), depth_(depth) {
        terrain_.resize(width_ * height_ * depth_);
    }

    void generateTerrain() {
        std::random_device rd;
        std::mt19937 generator(rd());
        std::uniform_real_distribution<float> distribution(-1.0f, 1.0f);

        for (int z = 0; z < depth_; ++z) {
            for (int y = 0; y < height_; ++y) {
                for (int x = 0; x < width_; ++x) {
                    float noise = distribution(generator);
                    int index = x + y * width_ + z * width_ * height_;
                    terrain_[index] = noise;
                }
            }
        }
    }

    void saveTerrainToFile(const std::string& filename) {
        // Implement code to save the generated terrain to a file (e.g., a heightmap).
        // This can vary depending on the file format you want to support.
        // You might use libraries like stb_image or write your custom file format.
        // Remember to handle any necessary error checking.
    }

private:
    int width_;
    int height_;
    int depth_;
    std::vector<float> terrain_;
};

int main() {
    int width = 512;
    int height = 512;
    int depth = 64;

    TerrainGenerator terrainGen(width, height, depth);
    terrainGen.generateTerrain();
    terrainGen.saveTerrainToFile("terrain_heightmap.png");  // Change the filename and format as needed.

    std::cout << "Terrain generation completed." << std::endl;

    return 0;
}
