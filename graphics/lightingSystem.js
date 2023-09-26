class LightingSystem {
  constructor() {
    this.lights = [];
  }

  addLight(light) {
    this.lights.push(light);
  }

  removeLight(light) {
    const index = this.lights.indexOf(light);
    if (index !== -1) {
      this.lights.splice(index, 1);
    }
  }

  update() {
    for (const light of this.lights) {
      // Update light properties based on game logic or input
      light.update();
    }
  }
}
