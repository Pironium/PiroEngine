#include <iostream>
#include <vector>
#include <cmath>

class WaterSurfaceGenerator {
public:
    WaterSurfaceGenerator(int width, int height) : width(width), height(height) {
        surface.reserve(width * height);
        generateSurface();
    }

    void generateSurface() {
        for (int x = 0; x < width; ++x) {
            for (int y = 0; y < height; ++y) {
                float value = calculateWaveHeight(x, y);
                surface.push_back(value);
            }
        }
    }

    float calculateWaveHeight(int x, int y) {
        float time = 0.0f; // Simulated time
        float frequency = 0.1f;
        float amplitude = 5.0f;

        float waveHeight = amplitude * sin(2 * M_PI * frequency * sqrt(x * x + y * y) - time);
        return waveHeight;
    }

private:
    int width;
    int height;
    std::vector<float> surface;
};

int main() {
    int width = 1920;
    int height = 1080;

    WaterSurfaceGenerator waterSurface(width, height);

    // Now you have a realistic water surface in the 'surface' vector.
    // You can use this data for rendering water in your games.
    
    return 0;
}
