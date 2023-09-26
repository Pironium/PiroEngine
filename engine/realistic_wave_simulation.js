class RealisticWaveSimulation {
  constructor(width, height) {
    this.width = width;
    this.height = height;
    this.waveData = new Array(width * height).fill(0);
    this.damping = 0.99;
    this.time = 0;
  }

  update() {
    const newWaveData = new Array(this.width * this.height).fill(0);

    for (let x = 1; x < this.width - 1; x++) {
      for (let y = 1; y < this.height - 1; y++) {
        const waveValue =
          (this.waveData[(x - 1) * this.width + y] +
            this.waveData[(x + 1) * this.width + y] +
            this.waveData[x * this.width + y - 1] +
            this.waveData[x * this.width + y + 1]) /
          2 -
          newWaveData[x * this.width + y];

        newWaveData[x * this.width + y] = waveValue * this.damping;
      }
    }

    this.waveData = newWaveData;
    this.time += 0.1;
  }
}
