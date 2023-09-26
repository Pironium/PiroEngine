#pragma once

#include <vector>
#include <glm/glm.hpp>

class ParticleSystem {
public:
    ParticleSystem(int maxParticles);

    void initialize();
    void update(float deltaTime);
    void render();

    void setEmitterPosition(const glm::vec3& position);
    void setEmitterDirection(const glm::vec3& direction);

private:
    struct Particle {
        glm::vec3 position;
        glm::vec3 velocity;
        float lifetime;
    };

    int maxParticles;
    std::vector<Particle> particles;
    glm::vec3 emitterPosition;
    glm::vec3 emitterDirection;
};
