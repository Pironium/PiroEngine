import json

class TranslationManager:
    def __init__(self):
        self.translations = {}

    def add_translation(self, language, key, value):
        if language not in self.translations:
            self.translations[language] = {}
        self.translations[language][key] = value

    def save_translations_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.translations, file, ensure_ascii=False, indent=4)

    def load_translations_from_json(self, filename):
        with open(filename, 'r') as file:
            self.translations = json.load(file)

    def get_translation(self, language, key):
        if language in self.translations and key in self.translations[language]:
            return self.translations[language][key]
        else:
            return f"Translation not found for key: {key}"

# Example usage:
if __name__ == "__main__":
    translator = TranslationManager()
    translator.add_translation("en", "hello", "Hello, World!")
    translator.add_translation("fr", "hello", "Bonjour, le Monde!")
    translator.save_translations_to_json("translations.json")

    translator.load_translations_from_json("translations.json")
    print(translator.get_translation("en", "hello"))
    print(translator.get_translation("fr", "hello"))
