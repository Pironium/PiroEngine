function generateFractalTerrain(width, height, detailLevel) {
  const terrain = new Array(width);

  // Initialize terrain with random values
  for (let x = 0; x < width; x++) {
    terrain[x] = new Array(height);
    for (let y = 0; y < height; y++) {
      terrain[x][y] = Math.random();
    }
  }

  // Perform fractal terrain generation using the Diamond-Square algorithm
  const diamondSquare = (x, y, size, roughness) => {
    if (size < 2) return;

    const half = size / 2;
    const average = (terrain[x][y] + terrain[x + size][y] + terrain[x][y + size] + terrain[x + size][y + size]) / 4;

    // Diamond step
    terrain[x + half][y + half] = average + (Math.random() * 2 - 1) * roughness;

    // Square step
    terrain[x + half][y] = (terrain[x][y] + terrain[x + size][y] + terrain[x + half][y + half]) / 3 + (Math.random() * 2 - 1) * roughness;
    terrain[x][y + half] = (terrain[x][y] + terrain[x][y + size] + terrain[x + half][y + half]) / 3 + (Math.random() * 2 - 1) * roughness;
    terrain[x + size][y + half] = (terrain[x + size][y] + terrain[x + size][y + size] + terrain[x + half][y + half]) / 3 + (Math.random() * 2 - 1) * roughness;
    terrain[x + half][y + size] = (terrain[x][y + size] + terrain[x + size][y + size] + terrain[x + half][y + half]) / 3 + (Math.random() * 2 - 1) * roughness;

    // Recursive calls for the four quadrants
    diamondSquare(x, y, half, roughness / 2);
    diamondSquare(x + half, y, half, roughness / 2);
    diamondSquare(x, y + half, half, roughness / 2);
    diamondSquare(x + half, y + half, half, roughness / 2);
  };

  diamondSquare(0, 0, width - 1, 1.0);

  return terrain;
}
