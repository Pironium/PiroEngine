#pragma once

#include "math/vector3.h"
#include "graphics/rendering/shader.h"

namespace PiroEngine {

  // Particle physics engine class
  class ParticlePhysicsEngine {
  public:
    ParticlePhysicsEngine() {}

    // Simulate particle physics
    void SimulatePhysics(float deltaTime) {
      // Complex physics simulation code goes here
      // ...
    }

    // Render particles with a custom shader effect
    void RenderParticles(Shader& customShader, const Vector3& cameraPosition) {
      // Rendering code with custom shader effect goes here
      // ...
    }
  };

} // namespace PiroEngine
