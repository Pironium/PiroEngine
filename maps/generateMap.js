// Import necessary libraries
import { Map, Tile, Tileset } from 'PiroEngine';

/**
 * Generate a new game map with specified dimensions and tileset.
 * @param {number} width - Width of the map.
 * @param {number} height - Height of the map.
 * @param {Tileset} tileset - Tileset to be used for the map.
 * @returns {Map} - The generated map.
 */
function generateMap(width, height, tileset) {
  // Create a new map with the given dimensions
  const map = new Map(width, height);

  // Fill the map with tiles from the provided tileset
  for (let x = 0; x < width; x++) {
    for (let y = 0; y < height; y++) {
      // Randomly select a tile from the tileset
      const randomTile = tileset.getRandomTile();
      map.setTile(x, y, randomTile);
    }
  }

  // Return the generated map
  return map;
}

// Export the generateMap function
export default generateMap;
