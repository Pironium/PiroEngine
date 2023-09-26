#include <iostream>
#include <cmath>

// New function: Calculate the gravitational force between two objects
double calculateGravitationalForce(double mass1, double mass2, double distance) {
    const double gravitationalConstant = 6.67430e-11; // Universal gravitational constant (m^3 kg^-1 s^-2)
    return (gravitationalConstant * mass1 * mass2) / (distance * distance);
}

int main() {
    double massObject1 = 1000.0; // Mass of the first object in kilograms
    double massObject2 = 1500.0; // Mass of the second object in kilograms
    double distanceBetweenObjects = 10.0; // Distance between the objects in meters

    // Calculate gravitational force between the two objects
    double gravitationalForce = calculateGravitationalForce(massObject1, massObject2, distanceBetweenObjects);

    std::cout << "Gravitational Force: " << gravitationalForce << " N" << std::endl;

    return 0;
}
