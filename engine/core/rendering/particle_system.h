#pragma once

#include <vector>
#include "math/vector3.h"
#include "graphics/shader.h"

class ParticleSystem {
public:
    ParticleSystem();

    void Initialize(int maxParticles);
    void Emit(const Vector3& position, const Vector3& velocity, float lifetime);
    void Update(float deltaTime);
    void Render(const Shader& shader);

private:
    struct Particle {
        Vector3 position;
        Vector3 velocity;
        float lifetime;
    };

    std::vector<Particle> particles;
    int maxParticles;
    int activeParticles;
    GLuint VAO, VBO;
};
