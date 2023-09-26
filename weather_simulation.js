// PiroEngine/Features/weather_simulation.js

class WeatherSimulation {
  constructor() {
    this.weatherConditions = ["Clear", "Cloudy", "Rainy", "Stormy"];
    this.currentWeather = "Clear";
  }

  changeWeather() {
    const randomIndex = Math.floor(Math.random() * this.weatherConditions.length);
    this.currentWeather = this.weatherConditions[randomIndex];
  }

  getCurrentWeather() {
    return this.currentWeather;
  }

  simulateWeatherChange() {
    setInterval(() => {
      this.changeWeather();
      console.log(`Weather changed to ${this.currentWeather}`);
    }, 60000); // Simulate weather change every 60 seconds
  }
}

module.exports = WeatherSimulation;
