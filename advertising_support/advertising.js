// Рекламный модуль для PiroEngine

// Класс для управления рекламными баннерами
class AdvertisingManager {
  constructor() {
    this.banners = [];
  }

  // Метод для добавления рекламного баннера
  addBanner(banner) {
    this.banners.push(banner);
  }

  // Метод для отображения всех рекламных баннеров
  showBanners() {
    for (const banner of this.banners) {
      banner.display();
    }
  }
}

// Класс для представления рекламного баннера
class AdBanner {
  constructor(content) {
    this.content = content;
  }

  // Метод для отображения рекламного баннера
  display() {
    console.log(`Displaying ad: ${this.content}`);
    // Здесь можно добавить логику отображения баннера в игре
  }
}

module.exports = { AdvertisingManager, AdBanner };
