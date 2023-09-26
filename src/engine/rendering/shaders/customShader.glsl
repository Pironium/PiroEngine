// Custom Shader for PiroEngine
#version 330 core

uniform vec3 objectColor;
uniform vec3 lightColor;

in vec3 FragPos;
in vec3 Normal;

out vec4 FragColor;

void main()
{
    // Calculate the lighting intensity
    vec3 ambient = 0.3 * lightColor;
    vec3 norm = normalize(Normal);
    vec3 lightDir = normalize(vec3(1.0, 1.0, 1.0)); // Example light direction

    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = diff * lightColor;

    vec3 result = (ambient + diffuse) * objectColor;
    FragColor = vec4(result, 1.0);
}
