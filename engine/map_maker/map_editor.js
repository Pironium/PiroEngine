// Map Editor Class for PiroEngine
class MapEditor {
  constructor() {
    this.mapData = {
      width: 0,
      height: 0,
      tiles: [],
    };
    this.tileset = null;
  }

  // Initialize the map with dimensions
  initMap(width, height) {
    this.mapData.width = width;
    this.mapData.height = height;

    for (let y = 0; y < height; y++) {
      let row = [];
      for (let x = 0; x < width; x++) {
        row.push(0); // Initialize with default tile ID
      }
      this.mapData.tiles.push(row);
    }
  }

  // Load a tileset for map editing
  loadTileset(tilesetURL) {
    this.tileset = new Tileset(tilesetURL);
  }

  // Set a tile at a specific position
  setTile(x, y, tileID) {
    if (x >= 0 && x < this.mapData.width && y >= 0 && y < this.mapData.height) {
      this.mapData.tiles[y][x] = tileID;
    }
  }

  // Export the map data as JSON
  exportMap() {
    return JSON.stringify(this.mapData);
  }

  // Import map data from JSON
  importMap(jsonData) {
    this.mapData = JSON.parse(jsonData);
  }
}

// Tileset Class for PiroEngine
class Tileset {
  constructor(url) {
    this.url = url;
    // Load the tileset image and other data
    // Add methods for managing tiles
  }
}

// Example usage:
const mapEditor = new MapEditor();
mapEditor.initMap(10, 10);
mapEditor.loadTileset('tileset.png');
mapEditor.setTile(2, 3, 1);
mapEditor.setTile(5, 7, 2);

const mapJSON = mapEditor.exportMap();
console.log(mapJSON);

// Later, you can import the map data:
// mapEditor.importMap(mapJSON);
