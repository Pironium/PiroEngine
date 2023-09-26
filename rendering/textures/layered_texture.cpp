#include <vector>
#include <iostream>

class LayeredTexture {
public:
    LayeredTexture(int width, int height) : width_(width), height_(height) {
        layers_.reserve(10); // Allow up to 10 layers
    }

    void AddLayer(const std::string& texturePath, float opacity) {
        if (layers_.size() < 10) { // Check if there's room for a new layer
            layers_.push_back({texturePath, opacity});
        } else {
            std::cout << "Max layer limit reached. Cannot add more layers." << std::endl;
        }
    }

    void Render() {
        // Code for rendering the layered texture with blending based on opacity
        // This would involve complex graphics operations, shaders, and more.
        // For brevity, we won't implement the entire rendering process here.
        std::cout << "Rendering layered texture..." << std::endl;
    }

private:
    int width_;
    int height_;
    struct Layer {
        std::string texturePath;
        float opacity;
    };
    std::vector<Layer> layers_;
};

int main() {
    LayeredTexture layeredTexture(1024, 768);
    layeredTexture.AddLayer("textures/layer1.png", 0.7);
    layeredTexture.AddLayer("textures/layer2.png", 0.5);
    layeredTexture.Render();

    return 0;
}
