// PiroEngine - Физический движок

class PhysicsEngine {
  constructor() {
    this.objects = [];
  }

  addObject(object) {
    this.objects.push(object);
  }

  removeObject(object) {
    const index = this.objects.indexOf(object);
    if (index !== -1) {
      this.objects.splice(index, 1);
    }
  }

  update(deltaTime) {
    // Выполнить расчеты физики для каждого объекта
    for (const object of this.objects) {
      if (object.isDynamic) {
        // Применить гравитацию
        object.applyGravity();

        // Выполнить обработку столкновений
        for (const otherObject of this.objects) {
          if (object !== otherObject) {
            if (object.isCollidingWith(otherObject)) {
              object.handleCollision(otherObject);
            }
          }
        }

        // Обновить положение объекта на основе физики
        object.updatePosition(deltaTime);
      }
    }
  }
}

module.exports = PhysicsEngine;
