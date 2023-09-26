class DynamicTextureGenerator {
  constructor(width, height) {
    this.width = width;
    this.height = height;
    this.canvas = document.createElement('canvas');
    this.canvas.width = width;
    this.canvas.height = height;
    this.context = this.canvas.getContext('2d');
  }

  generateNoiseTexture() {
    const imageData = this.context.createImageData(this.width, this.height);

    for (let i = 0; i < this.width * this.height * 4; i += 4) {
      const r = Math.floor(Math.random() * 256);
      const g = Math.floor(Math.random() * 256);
      const b = Math.floor(Math.random() * 256);
      const a = 255;

      imageData.data[i] = r;
      imageData.data[i + 1] = g;
      imageData.data[i + 2] = b;
      imageData.data[i + 3] = a;
    }

    this.context.putImageData(imageData, 0, 0);
    return this.canvas.toDataURL();
  }
}

export default DynamicTextureGenerator;
