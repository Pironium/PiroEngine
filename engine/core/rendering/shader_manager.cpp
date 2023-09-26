#include "shader_manager.h"

// Реализация новой функции, позволяющей создавать сложные шейдеры
Shader createComplexShader(const std::string& vertexShaderSource, const std::string& fragmentShaderSource) {
    Shader shader;
    shader.compileShader(vertexShaderSource, fragmentShaderSource);
    return shader;
}

// Остальной код шейдер-менеджера
