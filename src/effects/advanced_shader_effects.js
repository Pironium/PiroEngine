// Advanced Shader Effects Module
class AdvancedShaderEffects {
  constructor() {
    this.effects = [];
  }

  // Register a new shader effect
  registerEffect(effectName, vertexShader, fragmentShader) {
    const effect = {
      name: effectName,
      vertexShader: vertexShader,
      fragmentShader: fragmentShader,
    };
    this.effects.push(effect);
  }

  // Apply a shader effect to a game object
  applyEffect(gameObject, effectName) {
    const effect = this.effects.find((e) => e.name === effectName);
    if (!effect) {
      console.error(`Effect "${effectName}" not found.`);
      return;
    }

    gameObject.setVertexShader(effect.vertexShader);
    gameObject.setFragmentShader(effect.fragmentShader);
  }
}

module.exports = AdvancedShaderEffects;
