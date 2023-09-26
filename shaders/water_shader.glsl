// Water Shader
#version 330 core

// Uniforms
uniform sampler2D reflectionTexture; // Reflection texture
uniform sampler2D refractionTexture; // Refraction texture
uniform sampler2D dudvMap; // DuDv map for distortion
uniform sampler2D normalMap; // Normal map for normals calculation
uniform vec3 cameraPosition; // Camera position
uniform float moveFactor; // Movement factor for distortion
uniform float waveStrength; // Strength of water waves

in vec2 TexCoords;
out vec4 FragColor;

void main()
{
    // Calculate distorted texture coordinates
    vec2 distortedTexCoords = TexCoords + texture(dudvMap, TexCoords).rg * 0.1 * waveStrength * sin(moveFactor);
    
    // Clamp distorted texture coordinates
    distortedTexCoords = clamp(distortedTexCoords, 0.0, 1.0);
    
    // Calculate reflection color
    vec3 reflectionColor = texture(reflectionTexture, distortedTexCoords).rgb;
    
    // Calculate refraction color
    vec3 refractionColor = texture(refractionTexture, TexCoords).rgb;
    
    // Calculate normal from normal map
    vec3 normal = normalize(texture(normalMap, distortedTexCoords).rgb * 2.0 - 1.0);
    
    // Calculate view direction
    vec3 viewDirection = normalize(cameraPosition - vec3(TexCoords, 0.0));
    
    // Calculate Fresnel effect
    float fresnel = max(dot(viewDirection, normal), 0.0);
    fresnel = pow(fresnel, 4.0);
    
    // Combine reflection and refraction with Fresnel effect
    vec3 finalColor = mix(reflectionColor, refractionColor, fresnel);
    
    FragColor = vec4(finalColor, 1.0);
}
