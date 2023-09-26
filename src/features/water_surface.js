// Import necessary libraries
import { Engine, Scene, MeshBuilder, StandardMaterial, Color3, Vector3 } from 'PiroEngine';

// Define a class for WaterSurface
class WaterSurface {
  constructor(scene) {
    // Create a water mesh
    this.waterMesh = MeshBuilder.CreateGround('waterSurface', { width: 10, height: 10 }, scene);

    // Apply a water material
    const waterMaterial = new StandardMaterial('waterMaterial', scene);
    waterMaterial.diffuseColor = new Color3(0.0, 0.5, 1.0); // Blue color for water
    waterMaterial.alpha = 0.8; // Transparency
    waterMaterial.specularColor = new Color3(0, 0, 0); // No specular reflection
    waterMaterial.freeze(); // Optimize the material
    this.waterMesh.material = waterMaterial;

    // Add some waves animation to the water
    scene.registerBeforeRender(() => {
      const time = performance.now() * 0.001;
      const vertices = this.waterMesh.getVerticesData('position');

      for (let i = 0; i < vertices.length; i += 3) {
        const x = vertices[i];
        const z = vertices[i + 2];
        const y = Math.sin(x * 0.5 + time) * 0.1 + Math.cos(z * 0.5 + time) * 0.1;
        vertices[i + 1] = y;
      }

      this.waterMesh.updateVerticesData('position', vertices);
    });
  }

  // Function to add the water surface to the scene
  addToScene(scene) {
    scene.addMesh(this.waterMesh);
  }
}

// Export the WaterSurface class
export default WaterSurface;
