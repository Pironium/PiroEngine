class WaterSimulation {
  constructor(width, height) {
    this.width = width;
    this.height = height;
    this.waterMap = new Float32Array(width * height);
    this.damping = 0.98;
  }

  // Initialize the water simulation with a disturbance at a specific point
  initializeDisturbance(x, y, strength) {
    this.waterMap[x + y * this.width] = strength;
  }

  // Simulate water dynamics over time
  simulate() {
    const newWaterMap = new Float32Array(this.width * this.height);

    for (let x = 1; x < this.width - 1; x++) {
      for (let y = 1; y < this.height - 1; y++) {
        const idx = x + y * this.width;
        const waterHeight = this.waterMap[idx];
        const avgHeight =
          (this.waterMap[idx - 1] +
            this.waterMap[idx + 1] +
            this.waterMap[idx - this.width] +
            this.waterMap[idx + this.width]) /
          4.0;

        // Apply damping and simulate water flow
        const velocity = (avgHeight - waterHeight) * this.damping;
        newWaterMap[idx] = waterHeight + velocity;
      }
    }

    this.waterMap = newWaterMap;
  }

  // Get the current water height at a specific position
  getWaterHeight(x, y) {
    if (x >= 0 && x < this.width && y >= 0 && y < this.height) {
      return this.waterMap[x + y * this.width];
    } else {
      return 0.0;
    }
  }
}
