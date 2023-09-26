# Директория, в которой будет файл/i18n_manager.py

# Импортируем необходимые модули
import json

# Класс для управления интернационализацией
class I18nManager:
    def __init__(self, default_language='en'):
        self.default_language = default_language
        self.translations = {}

    def load_translations(self, language, translation_file):
        with open(translation_file, 'r', encoding='utf-8') as file:
            translations = json.load(file)
            self.translations[language] = translations

    def translate(self, language, key, default_value=''):
        if language in self.translations and key in self.translations[language]:
            return self.translations[language][key]
        elif self.default_language in self.translations and key in self.translations[self.default_language]:
            return self.translations[self.default_language][key]
        else:
            return default_value

# Пример использования
if __name__ == "__main__":
    i18n = I18nManager()

    # Загружаем переводы для разных языков
    i18n.load_translations('en', 'translations/en.json')
    i18n.load_translations('fr', 'translations/fr.json')

    # Используем переводы
    print(i18n.translate('en', 'welcome_message'))  # Выведет перевод на английском
    print(i18n.translate('fr', 'welcome_message'))  # Выведет перевод на французском
