// Complex fragment shader for advanced lighting effects
#version 330 core

uniform vec3 lightPosition;
uniform sampler2D diffuseTexture;
uniform sampler2D normalMap;

in vec2 TexCoords;
in vec3 FragPos;
in vec3 Normal;

out vec4 FragColor;

void main()
{
    vec3 lightDir = normalize(lightPosition - FragPos);
    vec3 normal = texture(normalMap, TexCoords).xyz * 2.0 - 1.0;
    normal = normalize(normal);
    
    float ambientStrength = 0.2;
    vec3 ambient = ambientStrength * vec3(1.0, 1.0, 1.0);
    
    float diff = max(dot(normal, lightDir), 0.0);
    vec3 diffuse = diff * vec3(1.0, 1.0, 1.0);
    
    float specularStrength = 0.5;
    vec3 viewDir = normalize(vec3(0.0, 0.0, -1.0) - FragPos);
    vec3 reflectDir = reflect(-lightDir, normal);
    float spec = pow(max(dot(viewDir, reflectDir), 0.0), 32);
    vec3 specular = specularStrength * spec * vec3(1.0, 1.0, 1.0);
    
    vec3 result = (ambient + diffuse + specular) * texture(diffuseTexture, TexCoords).xyz;
    FragColor = vec4(result, 1.0);
}
