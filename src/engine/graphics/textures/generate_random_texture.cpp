#include <iostream>
#include <vector>
#include <random>

class RandomTextureGenerator {
public:
    RandomTextureGenerator(int width, int height) : width_(width), height_(height) {}

    std::vector<unsigned char> GenerateRandomTexture() {
        std::vector<unsigned char> texture(width_ * height_ * 4); // RGBA format

        std::default_random_engine generator;
        std::uniform_int_distribution<int> distribution(0, 255);

        for (int i = 0; i < width_ * height_ * 4; ++i) {
            texture[i] = distribution(generator);
        }

        return texture;
    }

private:
    int width_;
    int height_;
};

int main() {
    int textureWidth = 512;
    int textureHeight = 512;

    RandomTextureGenerator textureGenerator(textureWidth, textureHeight);
    std::vector<unsigned char> randomTexture = textureGenerator.GenerateRandomTexture();

    // Now, you can use 'randomTexture' in your 3D engine for various purposes.
    std::cout << "Random texture generated successfully!" << std::endl;

    return 0;
}
