// i18n_support.js - Модуль для поддержки мультиязычности в PiroEngine

// Объект, хранящий переводы для разных языков
const translations = {};

/**
 * Функция для добавления перевода для конкретного языка
 * @param {string} language - Код языка (например, 'en' для английского)
 * @param {object} translationData - Объект с переводами для данного языка
 */
function addTranslation(language, translationData) {
  translations[language] = translationData;
}

/**
 * Функция для получения перевода строки для текущего языка
 * @param {string} key - Ключ строки для перевода
 * @returns {string} - Переведенная строка
 */
function translate(key) {
  // Получаем текущий язык пользователя (можно реализовать логику выбора языка)
  const currentLanguage = getCurrentLanguage(); // Предположим, что есть функция для определения текущего языка

  // Проверяем, есть ли перевод для данного ключа и языка
  if (translations[currentLanguage] && translations[currentLanguage][key]) {
    return translations[currentLanguage][key];
  }

  // Если перевод не найден, возвращаем оригинальную строку
  return key;
}

/**
 * Функция для получения текущего языка пользователя
 * @returns {string} - Код текущего языка (например, 'en' для английского)
 * Можно реализовать логику определения текущего языка здесь
 */

module.exports = {
  addTranslation,
  translate,
};
