// Рекламный модуль для PiroEngine

class AdvertisementManager {
  constructor(gameEngine) {
    this.gameEngine = gameEngine;
    this.advertisements = [];
  }

  // Функция для добавления рекламы
  addAdvertisement(advertisement) {
    this.advertisements.push(advertisement);
  }

  // Функция для отображения рекламы в игре
  displayAdvertisement() {
    if (this.advertisements.length === 0) {
      console.log("No advertisements to display.");
      return;
    }

    // Случайным образом выбираем рекламу для отображения
    const randomIndex = Math.floor(Math.random() * this.advertisements.length);
    const selectedAdvertisement = this.advertisements[randomIndex];

    // Отображаем рекламу в игровом окне
    console.log("Displaying advertisement:");
    console.log(selectedAdvertisement);

    // Здесь бы могла быть сложная логика отображения рекламы в игре, но для примера оставим это пустым.
  }
}

module.exports = AdvertisementManager;
