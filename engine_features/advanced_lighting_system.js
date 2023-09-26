/**
 * Advanced Lighting System for PiroEngine
 * 
 * This module provides advanced lighting capabilities for the PiroEngine.
 * It allows developers to create realistic lighting effects in their games.
 */

class AdvancedLightingSystem {
  constructor() {
    // Initialize lighting system
    this.lights = [];
    this.ambientLight = { r: 0.2, g: 0.2, b: 0.2 };
  }

  /**
   * Add a light source to the scene
   * @param {Object} position - The position of the light source
   * @param {Object} color - The color of the light source (RGB)
   * @param {number} intensity - The intensity of the light source
   */
  addLight(position, color, intensity) {
    const light = {
      position: position,
      color: color,
      intensity: intensity,
    };
    this.lights.push(light);
  }

  /**
   * Calculate lighting at a given point in the scene
   * @param {Object} point - The 3D point at which to calculate lighting
   * @returns {Object} - The resulting RGB color at the point
   */
  calculateLighting(point) {
    let resultColor = { r: this.ambientLight.r, g: this.ambientLight.g, b: this.ambientLight.b };

    for (const light of this.lights) {
      // Calculate distance and direction to the light source
      const direction = {
        x: light.position.x - point.x,
        y: light.position.y - point.y,
        z: light.position.z - point.z,
      };
      const distance = Math.sqrt(
        direction.x * direction.x + direction.y * direction.y + direction.z * direction.z
      );

      // Calculate light intensity at the point
      const intensity = light.intensity / (distance * distance);

      // Calculate diffuse reflection
      const dotProduct = direction.x * point.normal.x + direction.y * point.normal.y + direction.z * point.normal.z;
      if (dotProduct > 0) {
        resultColor.r += light.color.r * dotProduct * intensity;
        resultColor.g += light.color.g * dotProduct * intensity;
        resultColor.b += light.color.b * dotProduct * intensity;
      }
    }

    return resultColor;
  }
}

module.exports = AdvancedLightingSystem;
