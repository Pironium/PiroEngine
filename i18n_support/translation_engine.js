// translation_engine.js

// Define a class for translation support in the PiroEngine
class TranslationEngine {
  constructor() {
    this.translations = {}; // Initialize an empty translation dictionary
  }

  // Add a translation for a specific language
  addTranslation(language, translation) {
    if (!this.translations[language]) {
      this.translations[language] = {}; // Initialize a dictionary for the language
    }

    Object.assign(this.translations[language], translation); // Merge translations
  }

  // Translate a given string into the specified language
  translate(language, text) {
    if (this.translations[language] && this.translations[language][text]) {
      return this.translations[language][text];
    } else {
      // If translation is not found, return the original text
      return text;
    }
  }

  // List all available languages
  listLanguages() {
    return Object.keys(this.translations);
  }
}

// Export the TranslationEngine class
module.exports = TranslationEngine;
