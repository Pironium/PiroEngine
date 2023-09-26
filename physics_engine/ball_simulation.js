// PiroEngine - Физическая симуляция мяча

class Ball {
  constructor(x, y, radius) {
    this.x = x;
    this.y = y;
    this.radius = radius;
    this.velocityX = 0;
    this.velocityY = 0;
    this.mass = 1; // Масса мяча
  }

  // Метод для обновления положения мяча с учетом физики
  update() {
    const gravity = 9.8; // Ускорение свободного падения (м/с^2)

    // Применяем гравитацию
    this.velocityY += gravity;

    // Обновляем положение мяча
    this.x += this.velocityX;
    this.y += this.velocityY;

    // Обработка столкновений с границами экрана
    if (this.x - this.radius < 0) {
      this.x = this.radius;
      this.velocityX *= -1; // Отскок от левой границы
    }
    if (this.x + this.radius > screenWidth) {
      this.x = screenWidth - this.radius;
      this.velocityX *= -1; // Отскок от правой границы
    }
    if (this.y - this.radius < 0) {
      this.y = this.radius;
      this.velocityY *= -1; // Отскок от верхней границы
    }
    if (this.y + this.radius > screenHeight) {
      this.y = screenHeight - this.radius;
      this.velocityY *= -1; // Отскок от нижней границы
    }
  }

  // Метод для обработки столкновений с другими объектами
  handleCollisions(objects) {
    for (const object of objects) {
      if (object !== this) {
        const distance = Math.sqrt((this.x - object.x) ** 2 + (this.y - object.y) ** 2);
        if (distance < this.radius + object.radius) {
          // Столкновение с другим объектом
          const angle = Math.atan2(object.y - this.y, object.x - this.x);
          const overlap = this.radius + object.radius - distance;

          // Рассчитываем новые скорости после столкновения
          this.velocityX -= (overlap / 2) * Math.cos(angle) / this.mass;
          this.velocityY -= (overlap / 2) * Math.sin(angle) / this.mass;
        }
      }
    }
  }
}
