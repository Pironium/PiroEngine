#include <iostream>
#include <vector>

class PiroEngine {
private:
    std::vector<int> scene_objects;
    int current_frame;

public:
    PiroEngine() : current_frame(0) {}

    void addSceneObject(int object_id) {
        scene_objects.push_back(object_id);
    }

    void renderScene() {
        for (const auto& object : scene_objects) {
            // Render the object based on its ID and current frame
            renderObject(object, current_frame);
        }
        ++current_frame;
    }

private:
    void renderObject(int object_id, int frame) {
        // Implementation of rendering the object based on ID and frame
        std::cout << "Rendering object " << object_id << " at frame " << frame << "\n";
    }
};

int main() {
    PiroEngine piroEngine;
    piroEngine.addSceneObject(1);
    piroEngine.addSceneObject(2);

    // Simulate rendering 10 frames
    for (int i = 0; i < 10; ++i) {
        std::cout << "Rendering frame " << i << "\n";
        piroEngine.renderScene();
    }

    return 0;
}
