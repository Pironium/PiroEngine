// PiroEngine Level Generator

class LevelGenerator {
  constructor() {
    this.difficulty = 1;
  }

  setDifficulty(difficulty) {
    this.difficulty = difficulty;
  }

  generateLevel() {
    // Сложность уровня будет влиять на количество врагов, платформ и другие параметры
    const numEnemies = Math.floor(Math.random() * (10 * this.difficulty)) + 1;
    const numPlatforms = Math.floor(Math.random() * (5 * this.difficulty)) + 1;

    // Генерируем уровень с учетом сложности
    const level = {
      enemies: [],
      platforms: [],
    };

    for (let i = 0; i < numEnemies; i++) {
      const enemy = {
        x: Math.random() * 800,
        y: Math.random() * 600,
        type: Math.floor(Math.random() * 3), // 3 разных типа врагов
      };
      level.enemies.push(enemy);
    }

    for (let i = 0; i < numPlatforms; i++) {
      const platform = {
        x: Math.random() * 800,
        y: Math.random() * 100,
        width: Math.random() * 200 + 50,
        height: 20,
      };
      level.platforms.push(platform);
    }

    return level;
  }
}

module.exports = LevelGenerator;
