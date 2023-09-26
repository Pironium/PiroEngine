#include <iostream>
#include <vector>
#include <cmath>

class PhysicsEngine {
public:
    // Constructor
    PhysicsEngine() {
        gravity = {0.0, -9.81}; // Earth's gravity in m/s^2
        timeStep = 0.01; // Simulation time step in seconds
    }

    // Function to simulate physics
    void simulatePhysics(std::vector<GameObject>& objects) {
        for (GameObject& obj : objects) {
            // Apply gravity
            obj.applyForce(gravity * obj.getMass());

            // Update object's position and velocity
            obj.update(timeStep);
        }
    }

private:
    Vector2D gravity;
    double timeStep;
};

class Vector2D {
public:
    double x, y;

    // Constructor
    Vector2D(double x, double y) : x(x), y(y) {}

    // Overload + operator for vector addition
    Vector2D operator+(const Vector2D& other) const {
        return Vector2D(x + other.x, y + other.y);
    }

    // Overload * operator for scalar multiplication
    Vector2D operator*(double scalar) const {
        return Vector2D(x * scalar, y * scalar);
    }
};

class GameObject {
public:
    GameObject(const Vector2D& position, double mass) : position(position), mass(mass) {
        velocity = {0.0, 0.0};
        force = {0.0, 0.0};
    }

    void applyForce(const Vector2D& appliedForce) {
        force = force + appliedForce;
    }

    void update(double timeStep) {
        // Update velocity using Newton's second law
        Vector2D acceleration = force * (1.0 / mass);
        velocity = velocity + acceleration * timeStep;

        // Update position using velocity
        position = position + velocity * timeStep;

        // Reset force for the next iteration
        force = {0.0, 0.0};
    }

    double getMass() const {
        return mass;
    }

private:
    Vector2D position;
    Vector2D velocity;
    Vector2D force;
    double mass;
};
