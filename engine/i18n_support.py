# PiroEngine Internationalization (i18n) Support Module

# This module provides support for internationalization (i18n) in PiroEngine.

class I18nManager:
    def __init__(self):
        self.language = 'en'  # Default language is English

    def set_language(self, language_code):
        """
        Set the current language for the game.

        :param language_code: The language code (e.g., 'en' for English, 'fr' for French).
        """
        self.language = language_code

    def translate(self, text):
        """
        Translate the given text to the currently set language.

        :param text: The text to be translated.
        :return: Translated text in the current language.
        """
        translations = {
            'en': {
                'Welcome': 'Welcome',
                'Play': 'Play',
                'Settings': 'Settings',
                'Quit': 'Quit'
            },
            'fr': {
                'Welcome': 'Bienvenue',
                'Play': 'Jouer',
                'Settings': 'Paramètres',
                'Quit': 'Quitter'
            }
            # Add more translations for other languages as needed
        }

        translated_text = translations.get(self.language, {}).get(text, text)
        return translated_text
