class WeatherSystem {
  constructor() {
    this.currentWeather = 'clear'; // По умолчанию ясно
  }

  // Метод для установки текущей погоды
  setWeather(weather) {
    this.currentWeather = weather;
    this.applyWeatherEffects();
  }

  // Применение эффектов погоды
  applyWeatherEffects() {
    switch (this.currentWeather) {
      case 'clear':
        // Ясная погода - никаких эффектов
        break;
      case 'rain':
        // Дождь - добавить эффект дождя
        this.addRainEffect();
        break;
      case 'snow':
        // Снег - добавить эффект снега
        this.addSnowEffect();
        break;
      case 'storm':
        // Шторм - добавить эффект грозы
        this.addStormEffect();
        break;
      default:
        console.error('Unknown weather type');
    }
  }

  // Методы для добавления эффектов погоды
  addRainEffect() {
    // Реализация эффекта дождя
    // ...
  }

  addSnowEffect() {
    // Реализация эффекта снега
    // ...
  }

  addStormEffect() {
    // Реализация эффекта грозы
    // ...
  }
}

module.exports = WeatherSystem;
