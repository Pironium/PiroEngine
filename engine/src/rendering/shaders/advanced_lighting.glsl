// Advanced Lighting Shader
// This shader implements complex global illumination techniques

#version 330 core

// Uniforms
uniform mat4 viewProjectionMatrix;
uniform sampler2D albedoTexture;
uniform sampler2D normalMap;
uniform sampler2D irradianceMap;
uniform sampler2D reflectionMap;
uniform vec3 lightPosition;
uniform vec3 cameraPosition;

in vec2 fragTexCoord;
in vec3 fragNormal;

out vec4 fragColor;

void main()
{
    // Calculate lighting
    vec3 normal = normalize(texture(normalMap, fragTexCoord).rgb * 2.0 - 1.0);
    vec3 irradiance = texture(irradianceMap, normal).rgb;
    
    vec3 viewDir = normalize(cameraPosition - fragPosition);
    vec3 lightDir = normalize(lightPosition - fragPosition);
    float NdotL = max(dot(normal, lightDir), 0.0);
    
    vec3 reflection = normalize(reflect(-lightDir, normal));
    float RdotV = max(dot(reflection, viewDir), 0.0);
    
    // Implement complex lighting equation
    vec3 ambient = irradiance * albedoTexture.rgb * 0.03;
    vec3 diffuse = irradiance * albedoTexture.rgb * NdotL * 0.5;
    vec3 specular = irradiance * reflectionMap.rgb * pow(RdotV, 512.0) * 0.1;
    
    vec3 finalColor = ambient + diffuse + specular;
    
    fragColor = vec4(finalColor, 1.0);
}
