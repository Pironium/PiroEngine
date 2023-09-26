class DynamicEffect {
  constructor(mesh, parameters) {
    this.mesh = mesh;
    this.parameters = parameters;
    this.startTime = Date.now();
  }

  update() {
    const timeElapsed = (Date.now() - this.startTime) / 1000;

    // Применяем динамический эффект к мешу
    this.mesh.position.x = Math.sin(timeElapsed) * this.parameters.amplitudeX;
    this.mesh.position.y = Math.cos(timeElapsed) * this.parameters.amplitudeY;
    this.mesh.position.z = Math.sin(timeElapsed) * this.parameters.amplitudeZ;

    this.mesh.rotation.x = timeElapsed * this.parameters.rotationSpeedX;
    this.mesh.rotation.y = timeElapsed * this.parameters.rotationSpeedY;
    this.mesh.rotation.z = timeElapsed * this.parameters.rotationSpeedZ;
  }
}

// Добавляем новый метод в PiroEngine для создания динамических эффектов
PiroEngine.prototype.createDynamicEffect = function (mesh, parameters) {
  const dynamicEffect = new DynamicEffect(mesh, parameters);
  this.dynamicEffects.push(dynamicEffect);
};

// Инициализируем массив для хранения динамических эффектов
PiroEngine.prototype.dynamicEffects = [];
