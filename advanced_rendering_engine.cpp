#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

class RenderObject {
public:
    RenderObject(int id, const std::string& name) : id_(id), name_(name) {}

    void Render() {
        std::cout << "Rendering " << name_ << " (ID: " << id_ << ")" << std::endl;
    }

    void SetPosition(float x, float y, float z) {
        x_ = x;
        y_ = y;
        z_ = z;
        std::cout << "Setting position of " << name_ << " to (" << x_ << ", " << y_ << ", " << z_ << ")" << std::endl;
    }

private:
    int id_;
    std::string name_;
    float x_ = 0.0f;
    float y_ = 0.0f;
    float z_ = 0.0f;
};

class PiroEngine {
public:
    PiroEngine() {
        std::cout << "PiroEngine Initialized" << std::endl;
    }

    void AddObject(RenderObject object) {
        objects_.push_back(object);
        std::cout << "Added " << object.GetName() << " to the scene" << std::endl;
    }

    void RenderScene() {
        std::cout << "Rendering Scene:" << std::endl;
        for (const auto& object : objects_) {
            object.Render();
        }
    }

    void MoveObject(int objectId, float x, float y, float z) {
        auto it = std::find_if(objects_.begin(), objects_.end(), [objectId](const RenderObject& obj) {
            return obj.GetId() == objectId;
        });

        if (it != objects_.end()) {
            it->SetPosition(x, y, z);
        } else {
            std::cout << "Object with ID " << objectId << " not found in the scene" << std::endl;
        }
    }

private:
    std::vector<RenderObject> objects_;
};

int main() {
    PiroEngine engine;

    RenderObject object1(1, "Cube");
    RenderObject object2(2, "Sphere");

    engine.AddObject(object1);
    engine.AddObject(object2);

    engine.RenderScene();

    engine.MoveObject(1, 5.0f, 3.0f, -2.0f);

    engine.RenderScene();

    return 0;
}
