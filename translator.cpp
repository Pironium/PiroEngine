// translator.cpp

#include <iostream>
#include <string>
#include <unordered_map>

class CodeTranslator {
public:
    CodeTranslator() {
        // Инициализируем словарь, который будет содержать правила перевода
        initializeTranslationRules();
    }

    std::string translateToCpp(const std::string& inputCode, const std::string& sourceLanguage) {
        // Проверяем, есть ли правила перевода для указанного языка
        if (translationRules.find(sourceLanguage) == translationRules.end()) {
            return "Перевод из указанного языка не поддерживается.";
        }

        std::string cppCode = inputCode;

        // Применяем правила перевода
        for (const auto& rule : translationRules[sourceLanguage]) {
            size_t pos = 0;
            while ((pos = cppCode.find(rule.first, pos)) != std::string::npos) {
                cppCode.replace(pos, rule.first.length(), rule.second);
                pos += rule.second.length();
            }
        }

        return cppCode;
    }

private:
    std::unordered_map<std::string, std::unordered_map<std::string, std::string>> translationRules;

    void initializeTranslationRules() {
        // Здесь добавляем правила перевода для различных языков
        // Например, правило для перевода из Python в C++
        translationRules["Python"] = {
            {"print", "std::cout <<"},
            {"def", "void"},
            // Добавьте дополнительные правила по необходимости
        };

        // Добавьте правила для других языков программирования
    }
};

int main() {
    CodeTranslator translator;
    std::string sourceLanguage = "Python"; // Укажите язык, из которого нужно перевести
    std::string inputCode = "print('Hello, World!')"; // Пример кода на указанном языке

    std::string cppCode = translator.translateToCpp(inputCode, sourceLanguage);
    std::cout << "Translated C++ code:\n" << cppCode << std::endl;

    return 0;
}
