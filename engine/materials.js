// Define a Material class for 3D graphics
class Material {
  constructor(name, diffuseColor, specularColor, shininess) {
    this.name = name;
    this.diffuseColor = diffuseColor;
    this.specularColor = specularColor;
    this.shininess = shininess;
  }

  // Set the diffuse color of the material
  setDiffuseColor(color) {
    this.diffuseColor = color;
  }

  // Set the specular color of the material
  setSpecularColor(color) {
    this.specularColor = color;
  }

  // Set the shininess of the material
  setShininess(shininess) {
    this.shininess = shininess;
  }

  // Get the material properties as a JSON object
  toJSON() {
    return {
      name: this.name,
      diffuseColor: this.diffuseColor,
      specularColor: this.specularColor,
      shininess: this.shininess,
    };
  }
}

// Export the Material class
module.exports = Material;
