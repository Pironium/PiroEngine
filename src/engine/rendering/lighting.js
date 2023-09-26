class DynamicLight {
  constructor(position, color, intensity) {
    this.position = position; // 3D координаты источника света
    this.color = color;       // Цвет света (RGB)
    this.intensity = intensity; // Интенсивность света
  }

  // Метод для обновления положения света
  updatePosition(newPosition) {
    this.position = newPosition;
  }
}

function addDynamicLight(scene, light) {
  // Добавляем источник света в сцену
  scene.lights.push(light);
}

// Другие функции и методы для работы с освещением могут быть добавлены здесь

export { DynamicLight, addDynamicLight };
