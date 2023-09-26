// landscape_generator.js

/**
 * Генерирует случайный трехмерный ландшафт для игры.
 * @param {number} width - Ширина ландшафта в метрах.
 * @param {number} length - Длина ландшафта в метрах.
 * @param {number} maxHeight - Максимальная высота ландшафта.
 * @param {number} complexity - Сложность ландшафта (чем больше, тем более сложный ландшафт).
 * @returns {Array} - Двумерный массив, представляющий трехмерный ландшафт.
 */
function generateRandomLandscape(width, length, maxHeight, complexity) {
  const landscape = [];

  for (let x = 0; x < width; x++) {
    const row = [];
    for (let z = 0; z < length; z++) {
      const height = Math.random() * maxHeight;
      // Добавляем сложность, чтобы сделать ландшафт более разнообразным
      for (let c = 0; c < complexity; c++) {
        height += (Math.random() - 0.5) * maxHeight / complexity;
      }
      row.push(height);
    }
    landscape.push(row);
  }

  return landscape;
}

module.exports = {
  generateRandomLandscape,
};
