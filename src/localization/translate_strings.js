/**
 * Translate engine strings into multiple languages using JSON format.
 * @param {string} language - The target language for translation.
 * @returns {Object} - JSON object containing translated strings.
 */
function translateStrings(language) {
  let translations = {};

  if (language === 'en') {
    translations = {
      welcomeMessage: 'Welcome to PiroEngine!',
      playButton: 'Play',
      settings: 'Settings',
      exit: 'Exit',
      // Add more English translations here
    };
  } else if (language === 'fr') {
    translations = {
      welcomeMessage: 'Bienvenue dans PiroEngine !',
      playButton: 'Jouer',
      settings: 'Paramètres',
      exit: 'Quitter',
      // Add more French translations here
    };
  } else if (language === 'es') {
    translations = {
      welcomeMessage: '¡Bienvenido a PiroEngine!',
      playButton: 'Jugar',
      settings: 'Ajustes',
      exit: 'Salir',
      // Add more Spanish translations here
    };
  }
  // Add more language translations as needed

  return translations;
}

module.exports = translateStrings;
