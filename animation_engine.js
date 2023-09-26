// Директория, в которой будет файл/Название файла: graphics/
// Создадим класс для управления анимациями и визуальными эффектами
class AnimationEngine {
  constructor() {
    this.animations = [];
    this.effects = [];
  }

  // Метод для добавления анимации
  addAnimation(animation) {
    this.animations.push(animation);
  }

  // Метод для добавления визуального эффекта
  addEffect(effect) {
    this.effects.push(effect);
  }

  // Метод для обновления всех анимаций и эффектов
  update() {
    for (const animation of this.animations) {
      animation.update();
    }

    for (const effect of this.effects) {
      effect.apply();
    }
  }
}

// Директория, в которой будет файл/Название файла: main/
// Создадим экземпляр движка анимаций и эффектов
const animationEngine = new AnimationEngine();

// Добавим пример анимации - движение объекта
class MoveAnimation {
  constructor(object, targetX, targetY, duration) {
    this.object = object;
    this.targetX = targetX;
    this.targetY = targetY;
    this.duration = duration;
    this.startTime = Date.now();
  }

  update() {
    const currentTime = Date.now();
    const elapsedTime = currentTime - this.startTime;
    const progress = Math.min(elapsedTime / this.duration, 1);
    
    const newX = this.object.x + (this.targetX - this.object.x) * progress;
    const newY = this.object.y + (this.targetY - this.object.y) * progress;
    
    this.object.setPosition(newX, newY);

    if (progress === 1) {
      // Анимация завершена, удаляем ее из списка
      animationEngine.animations.splice(animationEngine.animations.indexOf(this), 1);
    }
  }
}

// Добавим пример визуального эффекта - мерцание объекта
class FlashEffect {
  constructor(object, duration) {
    this.object = object;
    this.duration = duration;
    this.startTime = Date.now();
    this.isVisible = true;
  }

  apply() {
    const currentTime = Date.now();
    const elapsedTime = currentTime - this.startTime;
    
    if (elapsedTime > this.duration) {
      this.isVisible = !this.isVisible;
      this.startTime = currentTime;
    }
    
    this.object.setVisible(this.isVisible);
  }
}

// Добавим объект на сцену
const gameObject = {
  x: 0,
  y: 0,
  setPosition: function (x, y) {
    this.x = x;
    this.y = y;
    console.log(`Object moved to (${x}, ${y})`);
  },
  setVisible: function (visible) {
    console.log(`Object visibility set to ${visible}`);
  },
};

// Добавим анимацию и эффект к объекту
animationEngine.addAnimation(new MoveAnimation(gameObject, 100, 100, 2000));
animationEngine.addEffect(new FlashEffect(gameObject, 1000));

// Директория, в которой будет файл/Название файла: README.md
// Обновим README с описанием новой функциональности
