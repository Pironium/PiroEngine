#include "shader_manager.h"

namespace PiroEngine {

    ShaderManager::ShaderManager() {
        // Конструктор класса ShaderManager
        // Инициализируем необходимые переменные и ресурсы
        // ...
    }

    ShaderManager::~ShaderManager() {
        // Деструктор класса ShaderManager
        // Освобождаем ресурсы и память
        // ...
    }

    void ShaderManager::LoadShader(const std::string& shaderName, const std::string& vertexShaderFile, const std::string& fragmentShaderFile) {
        // Загрузка шейдера по имени и путям к файлам вершинного и фрагментного шейдеров
        // ...

        // Компиляция и привязка шейдера к программе
        // ...

        // Добавление шейдера в коллекцию
        // ...
    }

    void ShaderManager::UseShader(const std::string& shaderName) {
        // Установка активного шейдера
        // ...
    }

    void ShaderManager::SetShaderUniform(const std::string& shaderName, const std::string& uniformName, const ShaderUniformValue& value) {
        // Установка значения uniform-переменной в активном шейдере
        // ...
    }

    // Другие методы для управления шейдерами

} // namespace PiroEngine
