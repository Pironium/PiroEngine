#include <iostream>
#include <cmath>

class AdvancedPhysics {
public:
    void calculateGravity(float mass, float gravityConstant) {
        float gravitationalForce = mass * gravityConstant;
        std::cout << "Calculated gravitational force: " << gravitationalForce << " N" << std::endl;
    }

    void simulateFluidDynamics(float viscosity, float density, float velocity) {
        float dragForce = 0.5f * viscosity * density * velocity * velocity;
        std::cout << "Calculated drag force: " << dragForce << " N" << std::endl;
    }
};

int main() {
    AdvancedPhysics physics;

    // Calculate gravitational force
    physics.calculateGravity(10.0f, 9.81f);

    // Simulate fluid dynamics
    physics.simulateFluidDynamics(0.002f, 1.2f, 5.0f);

    return 0;
}
