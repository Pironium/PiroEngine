// PiroEngine Custom Shader

#version 330 core

// Uniforms
uniform vec3 lightPosition;
uniform vec3 objectColor;
uniform vec3 lightColor;

// Input from the vertex shader
in vec3 FragPos;
in vec3 Normal;

// Output color
out vec4 FragColor;

void main()
{
    // Phong lighting model
    float ambientStrength = 0.1;
    vec3 ambient = ambientStrength * lightColor;

    vec3 norm = normalize(Normal);
    vec3 lightDir = normalize(lightPosition - FragPos);
    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = diff * lightColor;

    float specularStrength = 0.5;
    vec3 viewDir = normalize(-FragPos);
    vec3 reflectDir = reflect(-lightDir, norm);
    float spec = pow(max(dot(viewDir, reflectDir), 0.0), 32);
    vec3 specular = specularStrength * spec * lightColor;

    vec3 result = (ambient + diffuse + specular) * objectColor;
    FragColor = vec4(result, 1.0);
}
