class ParticleEffectsManager {
  constructor() {
    this.activeEffects = [];
  }

  // Generate a unique effect ID
  generateEffectID() {
    return Math.random().toString(36).substring(2, 15);
  }

  // Create a new particle effect
  createParticleEffect(effectConfig) {
    const effectID = this.generateEffectID();
    const newEffect = {
      id: effectID,
      config: effectConfig,
      startTime: Date.now(),
    };
    this.activeEffects.push(newEffect);
    return effectID;
  }

  // Update active particle effects
  update() {
    const currentTime = Date.now();
    this.activeEffects = this.activeEffects.filter((effect) => {
      // Simulate particle behavior and update accordingly
      // ...

      // Check if the effect has expired
      const effectDuration = currentTime - effect.startTime;
      if (effectDuration >= effect.config.duration) {
        return false; // Remove expired effect
      }

      return true; // Keep active effect
    });
  }
}
