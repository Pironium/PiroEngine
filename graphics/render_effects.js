class RenderEffects {
  constructor() {
    this.effects = new Map();
  }

  // Добавляем новый эффект
  addEffect(effectName, shaderCode) {
    this.effects.set(effectName, shaderCode);
  }

  // Применяем эффект к объекту
  applyEffect(object, effectName) {
    if (this.effects.has(effectName)) {
      const shaderCode = this.effects.get(effectName);
      object.applyShader(shaderCode);
    }
  }

  // Удалить эффект
  removeEffect(effectName) {
    this.effects.delete(effectName);
  }
}
