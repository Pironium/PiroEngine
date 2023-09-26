// PiroEngine Shader: Dynamic Lighting

// Vertex Shader
#version 330 core

layout(location = 0) in vec3 inPosition;
layout(location = 1) in vec3 inNormal;
layout(location = 2) in vec2 inTexCoords;

out vec3 fragPosition;
out vec3 fragNormal;
out vec2 texCoords;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main()
{
    gl_Position = projection * view * model * vec4(inPosition, 1.0);
    fragPosition = vec3(model * vec4(inPosition, 1.0));
    fragNormal = mat3(transpose(inverse(model))) * inNormal;
    texCoords = inTexCoords;
}

// Fragment Shader
#version 330 core

in vec3 fragPosition;
in vec3 fragNormal;
in vec2 texCoords;

out vec4 fragColor;

uniform vec3 lightPosition;
uniform vec3 objectColor;
uniform vec3 lightColor;

void main()
{
    // Phong lighting model
    vec3 lightDirection = normalize(lightPosition - fragPosition);
    float ambientStrength = 0.1;
    vec3 ambient = ambientStrength * lightColor;
    
    float diff = max(dot(fragNormal, lightDirection), 0.0);
    vec3 diffuse = diff * lightColor;
    
    float specularStrength = 0.5;
    vec3 viewDirection = normalize(-fragPosition);
    vec3 reflectDirection = reflect(-lightDirection, fragNormal);
    float spec = pow(max(dot(viewDirection, reflectDirection), 0.0), 32);
    vec3 specular = specularStrength * spec * lightColor;
    
    vec3 result = (ambient + diffuse + specular) * objectColor;
    fragColor = vec4(result, 1.0);
}
