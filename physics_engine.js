// Директория: PiroEngine/physics_engine.js

class PhysicsEngine {
  constructor() {
    this.objects = [];
    this.gravity = 9.81; // Гравитационная постоянная (м/с^2)
  }

  // Функция для добавления объектов в симуляцию
  addObject(object) {
    this.objects.push(object);
  }

  // Функция для обновления физической модели объектов
  update() {
    for (const object of this.objects) {
      // Применяем гравитацию
      object.velocity.y -= this.gravity;

      // Здесь можно добавить другие физические эффекты, такие как столкновения и динамику движения
    }
  }
}

class GameObject {
  constructor() {
    this.position = { x: 0, y: 0, z: 0 };
    this.velocity = { x: 0, y: 0, z: 0 };
    this.mass = 1; // Масса объекта (кг)
  }

  // Функция для обновления положения объекта
  updatePosition() {
    this.position.x += this.velocity.x;
    this.position.y += this.velocity.y;
    this.position.z += this.velocity.z;
  }
}

// Пример использования PhysicsEngine
const engine = new PhysicsEngine();

const object1 = new GameObject();
object1.mass = 2;
engine.addObject(object1);

const object2 = new GameObject();
object2.mass = 1;
engine.addObject(object2);

// Обновление физической модели
engine.update();
object1.updatePosition();
object2.updatePosition();

console.log('Позиция объекта 1:', object1.position);
console.log('Позиция объекта 2:', object2.position);
