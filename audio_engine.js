// Директория: engine/audio_engine.js

// Здесь мы импортируем необходимые библиотеки для работы с аудио
import AudioContext from 'web-audio-api';

// Класс AudioEngine будет управлять всеми аспектами звуков в игре
class AudioEngine {
  constructor() {
    // Инициализируем аудио-контекст для работы с звуком
    this.audioContext = new AudioContext();

    // Создаем пустой объект для хранения звуковых ресурсов
    this.audioResources = {};

    // Метод для загрузки звуковых файлов
    this.loadSound = this.loadSound.bind(this);
  }

  // Метод для загрузки звуковых файлов
  loadSound(soundName, soundFileURL) {
    const request = new XMLHttpRequest();
    request.open('GET', soundFileURL, true);
    request.responseType = 'arraybuffer';

    request.onload = () => {
      this.audioContext.decodeAudioData(request.response, (buffer) => {
        // Сохраняем декодированный звук в ресурсы
        this.audioResources[soundName] = buffer;
      }, (error) => {
        console.error(`Ошибка при декодировании аудио: ${error}`);
      });
    };

    request.send();
  }

  // Метод для воспроизведения звука по имени
  playSound(soundName) {
    if (this.audioResources[soundName]) {
      const source = this.audioContext.createBufferSource();
      source.buffer = this.audioResources[soundName];
      source.connect(this.audioContext.destination);
      source.start();
    } else {
      console.error(`Звук "${soundName}" не найден в ресурсах.`);
    }
  }
}

// Экспортируем класс AudioEngine для использования в игре
export default AudioEngine;
