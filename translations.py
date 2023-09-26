class TranslationManager:
    def __init__(self):
        self.translations = {}

    def load_translation(self, language_code):
        try:
            with open(f'translations/{language_code}.json', 'r', encoding='utf-8') as file:
                self.translations[language_code] = json.load(file)
        except FileNotFoundError:
            print(f"Translation file for {language_code} not found!")

    def get_translation(self, language_code, key):
        if language_code in self.translations and key in self.translations[language_code]:
            return self.translations[language_code][key]
        else:
            return f"Translation not found for '{key}' in '{language_code}'"

    def add_translation(self, language_code, key, translation):
        if language_code not in self.translations:
            self.translations[language_code] = {}
        self.translations[language_code][key] = translation

    def save_translation(self, language_code):
        if language_code in self.translations:
            with open(f'translations/{language_code}.json', 'w', encoding='utf-8') as file:
                json.dump(self.translations[language_code], file, ensure_ascii=False, indent=4)

# Example usage:
translator = TranslationManager()
translator.load_translation('en')  # Load English translation
translator.add_translation('fr', 'hello', 'Bonjour')  # Add French translation for 'hello'
translator.save_translation('fr')  # Save French translation to 'translations/fr.json'
translation = translator.get_translation('fr', 'hello')  # Get French translation for 'hello'
print(translation)  # Output: Bonjour
