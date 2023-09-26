// PiroEngine Landscape Generation Module

class LandscapeGenerator {
  constructor() {
    this.heightMap = []; // Store heightmap data
  }

  generateHeightMap(width, height) {
    this.heightMap = []; // Clear previous heightmap data

    // Generate a random heightmap
    for (let y = 0; y < height; y++) {
      this.heightMap[y] = [];
      for (let x = 0; x < width; x++) {
        this.heightMap[y][x] = Math.random(); // Random height value (0 to 1)
      }
    }
  }

  applySmoothing(iterations) {
    // Apply smoothing to the heightmap
    for (let iter = 0; iter < iterations; iter++) {
      for (let y = 1; y < this.heightMap.length - 1; y++) {
        for (let x = 1; x < this.heightMap[y].length - 1; x++) {
          // Calculate the average of surrounding heights
          const avgHeight =
            (this.heightMap[y - 1][x - 1] +
              this.heightMap[y - 1][x] +
              this.heightMap[y - 1][x + 1] +
              this.heightMap[y][x - 1] +
              this.heightMap[y][x] +
              this.heightMap[y][x + 1] +
              this.heightMap[y + 1][x - 1] +
              this.heightMap[y + 1][x] +
              this.heightMap[y + 1][x + 1]) /
            9;

          // Update the height at (x, y) with the average
          this.heightMap[y][x] = avgHeight;
        }
      }
    }
  }

  exportHeightMap() {
    // Return the generated heightmap
    return this.heightMap;
  }
}

// Example usage:
const landscapeGen = new LandscapeGenerator();
landscapeGen.generateHeightMap(512, 512); // Generate a 512x512 heightmap
landscapeGen.applySmoothing(5); // Apply smoothing to make it more realistic
const heightMapData = landscapeGen.exportHeightMap();

// You can now use heightMapData to create 3D landscapes in PiroEngine.
