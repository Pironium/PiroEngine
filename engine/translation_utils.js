// Файл: translation_utils.js

/**
 * Функция для добавления переводов строк в JSON формате.
 * @param {string} text - Текст, который нужно перевести.
 * @param {string} language - Язык, на который нужно перевести текст.
 * @returns {string} - Строка в формате JSON с переводом.
 */
function translateTextToJson(text, language) {
  const translations = {
    en: text, // По умолчанию, если перевода нет, оставляем на английском.
    // Добавьте здесь переводы для других языков по необходимости.
    // Например: fr: 'Текст на французском',
    //          es: 'Текст на испанском',
  };

  return JSON.stringify({ [language]: translations[language] || text });
}

module.exports = {
  translateTextToJson,
};
