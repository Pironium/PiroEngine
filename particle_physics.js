// Директория: engine/graphics/effects/
// Название файла: particle_physics.js

class Particle {
  constructor(x, y, z, velocityX, velocityY, velocityZ, lifespan) {
    this.position = { x, y, z };
    this.velocity = { velocityX, velocityY, velocityZ };
    this.lifespan = lifespan;
  }

  update() {
    // Обновление позиции частицы на основе её скорости
    this.position.x += this.velocity.velocityX;
    this.position.y += this.velocity.velocityY;
    this.position.z += this.velocity.velocityZ;
    
    // Уменьшение оставшегося времени жизни частицы
    this.lifespan--;
  }
}

class ParticleSystem {
  constructor() {
    this.particles = [];
  }

  addParticle(particle) {
    this.particles.push(particle);
  }

  update() {
    // Обновление всех частиц в системе
    for (let i = this.particles.length - 1; i >= 0; i--) {
      const particle = this.particles[i];
      particle.update();
      
      // Удаление частиц, у которых закончился срок жизни
      if (particle.lifespan <= 0) {
        this.particles.splice(i, 1);
      }
    }
  }
}

// Использование:
const particleSystem = new ParticleSystem();

function createExplosion(x, y, z, numParticles) {
  for (let i = 0; i < numParticles; i++) {
    const velocityX = (Math.random() - 0.5) * 0.1;
    const velocityY = (Math.random() - 0.5) * 0.1;
    const velocityZ = (Math.random() - 0.5) * 0.1;
    const lifespan = 100 + Math.random() * 50;
    const particle = new Particle(x, y, z, velocityX, velocityY, velocityZ, lifespan);
    particleSystem.addParticle(particle);
  }
}

// Главный цикл игры
function gameLoop() {
  // Обновление системы частиц
  particleSystem.update();
  
  // Рендеринг частиц на экране
  // (добавьте вашу логику рендеринга здесь)
  
  requestAnimationFrame(gameLoop);
}

// Запуск игрового цикла
gameLoop();
