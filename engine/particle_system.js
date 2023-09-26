class ParticleSystem {
  constructor() {
    this.particles = [];
    this.isActive = false;
  }

  activate() {
    this.isActive = true;
  }

  deactivate() {
    this.isActive = false;
  }

  update() {
    if (this.isActive) {
      for (let i = this.particles.length - 1; i >= 0; i--) {
        const particle = this.particles[i];
        particle.update();
        if (particle.isDead()) {
          this.particles.splice(i, 1);
        }
      }
    }
  }

  render() {
    if (this.isActive) {
      for (const particle of this.particles) {
        particle.render();
      }
    }
  }

  addParticle(particle) {
    this.particles.push(particle);
  }
}

class Particle {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.velocityX = Math.random() * 2 - 1;
    this.velocityY = Math.random() * 2 - 1;
    this.size = Math.random() * 10 + 5;
    this.color = `rgba(${Math.random() * 255}, ${Math.random() * 255}, ${Math.random() * 255}, ${Math.random()})`;
    this.life = Math.random() * 100 + 50;
  }

  update() {
    this.x += this.velocityX;
    this.y += this.velocityY;
    this.life--;
  }

  render() {
    // Render the particle on the screen using canvas or any other graphics library
  }

  isDead() {
    return this.life <= 0;
  }
}

// Usage Example:
const particleSystem = new ParticleSystem();
particleSystem.activate();

function gameLoop() {
  particleSystem.update();
  particleSystem.render();
  requestAnimationFrame(gameLoop);
}

gameLoop();
