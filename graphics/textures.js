class TextureManager {
    constructor() {
        this.textures = new Map();
    }

    loadTexture(textureName, filePath) {
        // Load texture from file path and store it in the textures map
        const texture = loadTextureFromFile(filePath);
        this.textures.set(textureName, texture);
    }

    bindTexture(textureName) {
        // Bind the specified texture for rendering
        const texture = this.textures.get(textureName);
        if (texture) {
            bindTexture(texture);
        }
    }

    unloadTexture(textureName) {
        // Unload the specified texture from memory
        const texture = this.textures.get(textureName);
        if (texture) {
            unloadTexture(texture);
            this.textures.delete(textureName);
        }
    }
}

// Usage example:
const textureManager = new TextureManager();
textureManager.loadTexture('grass_texture', 'textures/grass.png');
textureManager.bindTexture('grass_texture');
