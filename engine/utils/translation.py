# PiroEngine Translation Utility

class TranslationManager:
    def __init__(self):
        self.translations = {}
    
    def add_translation(self, language, translation_data):
        if language not in self.translations:
            self.translations[language] = {}
        self.translations[language].update(translation_data)
    
    def get_translation(self, language, key):
        if language in self.translations and key in self.translations[language]:
            return self.translations[language][key]
        else:
            return f"Translation not found for key: {key}"

# Example usage:
translation_manager = TranslationManager()
translation_manager.add_translation("en", {
    "greeting": "Hello, World!",
    "instructions": "Press 'W' to move forward."
})
translation_manager.add_translation("fr", {
    "greeting": "Bonjour, le Monde!",
    "instructions": "Appuyez sur 'Z' pour avancer."
})

# Retrieve translations
current_language = "fr"
greeting_translation = translation_manager.get_translation(current_language, "greeting")
instructions_translation = translation_manager.get_translation(current_language, "instructions")

print(greeting_translation)
print(instructions_translation)
