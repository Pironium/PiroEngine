// Директория: engine_modules/
// Название файла: advertising_support.js

// Импорт необходимых модулей
const AdNetwork = require('./ad_network.js');
const GameAnalytics = require('./game_analytics.js');

class AdvertisingSupport {
  constructor() {
    this.adNetwork = new AdNetwork();
    this.analytics = new GameAnalytics();
  }

  // Метод для инициализации рекламы
  initializeAds() {
    this.adNetwork.init();
    this.analytics.trackEvent('AdsInitialized');
  }

  // Метод для показа рекламы перед началом игры
  showInterstitialAd() {
    if (this.adNetwork.isAdAvailable()) {
      this.adNetwork.showInterstitialAd();
      this.analytics.trackEvent('InterstitialAdShown');
    }
  }

  // Метод для показа рекламы во время игры
  showBannerAd() {
    if (this.adNetwork.isAdAvailable()) {
      this.adNetwork.showBannerAd();
      this.analytics.trackEvent('BannerAdShown');
    }
  }

  // Метод для обработки нажатия на рекламу
  handleAdClick() {
    this.analytics.trackEvent('AdClicked');
  }
}

module.exports = AdvertisingSupport;
