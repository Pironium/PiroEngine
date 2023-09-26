// Shader support for PiroEngine

// Define a struct to hold shader information
struct Shader {
    int shaderID;
    bool compiled;
    string log;
};

// Function to compile a shader
Shader compileShader(string vertexCode, string fragmentCode) {
    Shader shader;
    shader.shaderID = glCreateProgram();
    int vertexShader = glCreateShader(GL_VERTEX_SHADER);
    int fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);

    // Compile vertex shader
    glShaderSource(vertexShader, 1, vertexCode, NULL);
    glCompileShader(vertexShader);
    glGetShaderiv(vertexShader, GL_COMPILE_STATUS, &shader.compiled);

    if (!shader.compiled) {
        shader.log = glGetShaderInfoLog(vertexShader);
        return shader;
    }

    // Compile fragment shader
    glShaderSource(fragmentShader, 1, fragmentCode, NULL);
    glCompileShader(fragmentShader);
    glGetShaderiv(fragmentShader, GL_COMPILE_STATUS, &shader.compiled);

    if (!shader.compiled) {
        shader.log = glGetShaderInfoLog(fragmentShader);
        return shader;
    }

    // Attach shaders to the program and link
    glAttachShader(shader.shaderID, vertexShader);
    glAttachShader(shader.shaderID, fragmentShader);
    glLinkProgram(shader.shaderID);

    return shader;
}

// Function to use a shader program
void useShader(Shader shader) {
    if (shader.compiled) {
        glUseProgram(shader.shaderID);
    }
}

// Function to set uniform values in a shader
void setUniform(Shader shader, string name, float value) {
    if (shader.compiled) {
        int location = glGetUniformLocation(shader.shaderID, name);
        if (location != -1) {
            glUniform1f(location, value);
        }
    }
}

// Add more shader-related functions here as needed
