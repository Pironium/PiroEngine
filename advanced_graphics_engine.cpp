#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

// Define a 3D vector class for advanced graphics calculations
class Vector3D {
public:
    float x, y, z;

    Vector3D(float x, float y, float z) : x(x), y(y), z(z) {}

    Vector3D operator+(const Vector3D& other) const {
        return Vector3D(x + other.x, y + other.y, z + other.z);
    }

    Vector3D operator-(const Vector3D& other) const {
        return Vector3D(x - other.x, y - other.y, z - other.z);
    }

    Vector3D operator*(float scalar) const {
        return Vector3D(x * scalar, y * scalar, z * scalar);
    }

    float dot(const Vector3D& other) const {
        return x * other.x + y * other.y + z * other.z;
    }

    Vector3D cross(const Vector3D& other) const {
        return Vector3D(
            y * other.z - z * other.y,
            z * other.x - x * other.z,
            x * other.y - y * other.x
        );
    }

    float length() const {
        return std::sqrt(x * x + y * y + z * z);
    }

    Vector3D normalized() const {
        float len = length();
        return Vector3D(x / len, y / len, z / len);
    }
};

// Define a class for managing 3D meshes
class Mesh {
public:
    std::vector<Vector3D> vertices;
    std::vector<int> triangles;

    void addVertex(const Vector3D& vertex) {
        vertices.push_back(vertex);
    }

    void addTriangle(int v1, int v2, int v3) {
        triangles.push_back(v1);
        triangles.push_back(v2);
        triangles.push_back(v3);
    }
};

// Define a class for the PiroEngine
class PiroEngine {
public:
    Mesh createCube(float size) {
        Mesh cube;

        // Define cube vertices
        Vector3D v0(-size, -size, -size);
        Vector3D v1(-size, -size, size);
        Vector3D v2(-size, size, -size);
        Vector3D v3(-size, size, size);
        Vector3D v4(size, -size, -size);
        Vector3D v5(size, -size, size);
        Vector3D v6(size, size, -size);
        Vector3D v7(size, size, size);

        // Add vertices to the mesh
        cube.addVertex(v0);
        cube.addVertex(v1);
        cube.addVertex(v2);
        cube.addVertex(v3);
        cube.addVertex(v4);
        cube.addVertex(v5);
        cube.addVertex(v6);
        cube.addVertex(v7);

        // Define cube triangles
        cube.addTriangle(0, 1, 2);
        cube.addTriangle(1, 3, 2);
        cube.addTriangle(4, 6, 5);
        cube.addTriangle(5, 6, 7);
        cube.addTriangle(0, 4, 1);
        cube.addTriangle(1, 4, 5);
        cube.addTriangle(2, 3, 6);
        cube.addTriangle(3, 7, 6);
        cube.addTriangle(0, 2, 4);
        cube.addTriangle(2, 6, 4);
        cube.addTriangle(1, 5, 3);
        cube.addTriangle(3, 5, 7);

        return cube;
    }
};

int main() {
    PiroEngine engine;

    // Create a cube mesh
    Mesh cubeMesh = engine.createCube(1.0f);

    // Output the cube's vertices and triangles
    std::cout << "Cube Vertices:" << std::endl;
    for (const Vector3D& vertex : cubeMesh.vertices) {
        std::cout << "(" << vertex.x << ", " << vertex.y << ", " << vertex.z << ")" << std::endl;
    }

    std::cout << "Cube Triangles:" << std::endl;
    for (size_t i = 0; i < cubeMesh.triangles.size(); i += 3) {
        std::cout << "(" << cubeMesh.triangles[i] << ", " << cubeMesh.triangles[i + 1] << ", " << cubeMesh.triangles[i + 2] << ")" << std::endl;
    }

    return 0;
}
