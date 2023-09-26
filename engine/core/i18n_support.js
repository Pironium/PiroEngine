// i18n_support.js - Добавляем поддержку перевода строк

class I18nManager {
  constructor() {
    this.translations = {};
  }

  // Функция для добавления переводов
  addTranslation(languageCode, translations) {
    if (!this.translations[languageCode]) {
      this.translations[languageCode] = {};
    }

    for (const key in translations) {
      this.translations[languageCode][key] = translations[key];
    }
  }

  // Функция для получения перевода строки
  translate(languageCode, key) {
    if (this.translations[languageCode] && this.translations[languageCode][key]) {
      return this.translations[languageCode][key];
    } else {
      // Если перевод не найден, возвращаем оригинальную строку
      return key;
    }
  }
}

// Инициализация менеджера i18n
const i18nManager = new I18nManager();

// Пример добавления переводов для разных языков
i18nManager.addTranslation('en', {
  'hello': 'Hello',
  'world': 'World',
});

i18nManager.addTranslation('fr', {
  'hello': 'Bonjour',
  'world': 'Monde',
});

// Использование переводов
const currentLanguage = 'fr';
const translatedHello = i18nManager.translate(currentLanguage, 'hello');
const translatedWorld = i18nManager.translate(currentLanguage, 'world');

console.log(translatedHello); // Вывод: "Bonjour"
console.log(translatedWorld); // Вывод: "Monde"
