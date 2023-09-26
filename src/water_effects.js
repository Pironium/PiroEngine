// PiroEngine Water Effects Module

class WaterEffect {
  constructor(options) {
    this.mesh = options.mesh;
    this.waveHeight = options.waveHeight || 0.1;
    this.waveSpeed = options.waveSpeed || 0.05;
    this.time = 0;
  }

  update(deltaTime) {
    this.time += deltaTime;
    const vertices = this.mesh.geometry.vertices;
    
    for (let i = 0; i < vertices.length; i++) {
      const vertex = vertices[i];
      vertex.z = Math.sin(this.time * this.waveSpeed + vertex.x + vertex.y) * this.waveHeight;
    }

    this.mesh.geometry.verticesNeedUpdate = true;
  }
}

export { WaterEffect };
