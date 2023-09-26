class ParticleSystem {
  constructor() {
    this.particles = [];
  }

  // Create a burst of particles at a given position
  createParticleBurst(position, numParticles) {
    for (let i = 0; i < numParticles; i++) {
      const particle = new Particle(position);
      this.particles.push(particle);
    }
  }

  // Update all particles in the system
  update() {
    for (let i = this.particles.length - 1; i >= 0; i--) {
      const particle = this.particles[i];
      particle.update();
      if (particle.isDead()) {
        this.particles.splice(i, 1);
      }
    }
  }

  // Render all particles in the system
  render() {
    for (const particle of this.particles) {
      particle.render();
    }
  }
}

class Particle {
  constructor(position) {
    this.position = position;
    this.velocity = createRandomVector(); // Function to create a random vector
    this.size = random(5, 15);
    this.color = randomColor(); // Function to generate a random color
    this.lifespan = 255; // Initial lifespan of the particle
  }

  update() {
    this.position.add(this.velocity);
    this.lifespan -= 2;
  }

  render() {
    // Render the particle as a colored circle
    fill(this.color.r, this.color.g, this.color.b, this.lifespan);
    noStroke();
    ellipse(this.position.x, this.position.y, this.size);
  }

  isDead() {
    return this.lifespan <= 0;
  }
}

// Helper function to create a random vector
function createRandomVector() {
  const angle = random(TWO_PI);
  const magnitude = random(1);
  return createVector(cos(angle) * magnitude, sin(angle) * magnitude);
}

// Helper function to generate a random color
function randomColor() {
  return {
    r: random(255),
    g: random(255),
    b: random(255),
  };
}
