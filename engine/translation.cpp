#include <iostream>
#include <unordered_map>
#include <string>

// Создаем словарь для перевода языков программирования в C++
std::unordered_map<std::string, std::string> languageTranslation = {
    {"Python", "PythonToCppTranslator"},
    {"JavaScript", "JsToCppTranslator"},
    {"Java", "JavaToCppTranslator"},
    {"Ruby", "RubyToCppTranslator"},
    {"C#", "CSharpToCppTranslator"},
    // Добавьте сюда больше языков по желанию
};

std::string TranslateToCpp(const std::string& inputLanguage) {
    // Проверяем, есть ли язык в словаре
    if (languageTranslation.find(inputLanguage) != languageTranslation.end()) {
        return languageTranslation[inputLanguage];
    } else {
        return "TranslationNotAvailable";
    }
}

int main() {
    std::string inputLanguage;
    std::cout << "Введите язык программирования для перевода в C++: ";
    std::cin >> inputLanguage;
    
    std::string cppEquivalent = TranslateToCpp(inputLanguage);
    
    if (cppEquivalent == "TranslationNotAvailable") {
        std::cout << "Извините, перевод для данного языка программирования недоступен." << std::endl;
    } else {
        std::cout << "Эквивалент на C++: " << cppEquivalent << std::endl;
    }
    
    return 0;
}
