// PiroEngine Particle System

class ParticleSystem {
  constructor() {
    this.particles = [];
  }

  initialize() {
    // Initialize particle system here
  }

  emitParticle(x, y, z) {
    // Emit a new particle at the specified position
    const particle = new Particle(x, y, z);
    this.particles.push(particle);
  }

  update() {
    // Update all particles in the system
    for (let i = this.particles.length - 1; i >= 0; i--) {
      const particle = this.particles[i];
      if (particle.isAlive()) {
        particle.update();
      } else {
        // Remove dead particles
        this.particles.splice(i, 1);
      }
    }
  }
}

class Particle {
  constructor(x, y, z) {
    this.position = { x, y, z };
    this.velocity = { x: 0, y: 0, z: 0 };
    this.lifetime = 100; // Lifetime of the particle
    this.age = 0;
  }

  isAlive() {
    return this.age < this.lifetime;
  }

  update() {
    // Update particle position, velocity, and age here
    this.age++;
  }
}

// Export the ParticleSystem class for use in PiroEngine
module.exports = ParticleSystem;
