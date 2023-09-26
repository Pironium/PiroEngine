// PiroEngine Deferred Lighting Shader
// This shader implements a deferred lighting technique with advanced features

#version 330 core

// Uniforms
uniform sampler2D gPosition;
uniform sampler2D gNormal;
uniform sampler2D gAlbedoSpec;
uniform sampler2D gEmission;

// Lights
struct Light {
    vec3 position;
    vec3 color;
    float intensity;
};

uniform Light lights[8];
uniform int numLights;

out vec4 FragColor;

void main() {
    // Retrieve fragment data from G-buffer textures
    vec3 FragPos = texture(gPosition, gl_FragCoord.xy).xyz;
    vec3 Normal = texture(gNormal, gl_FragCoord.xy).xyz;
    vec3 Albedo = texture(gAlbedoSpec, gl_FragCoord.xy).xyz;
    vec3 Emission = texture(gEmission, gl_FragCoord.xy).xyz;
    
    vec3 lightingResult = vec3(0.0);

    // Calculate lighting contributions from all active lights
    for (int i = 0; i < numLights; ++i) {
        Light light = lights[i];
        
        // Calculate the light direction and distance
        vec3 lightDir = light.position - FragPos;
        float distance = length(lightDir);
        lightDir = normalize(lightDir);
        
        // Calculate attenuation
        float attenuation = 1.0 / (1.0 + 0.09 * distance + 0.032 * (distance * distance));
        
        // Diffuse lighting
        float diff = max(dot(Normal, lightDir), 0.0);
        vec3 diffuse = diff * light.color * light.intensity * Albedo;
        
        // Specular lighting (Phong reflection model)
        vec3 viewDir = normalize(-FragPos);
        vec3 reflectDir = reflect(-lightDir, Normal);
        float spec = pow(max(dot(viewDir, reflectDir), 0.0), 32.0);
        vec3 specular = spec * light.color * light.intensity;

        // Final light contribution for this light source
        vec3 result = (diffuse + specular) * attenuation;
        
        // Accumulate the lighting result
        lightingResult += result;
    }

    // Add emissive lighting
    lightingResult += Emission;
    
    FragColor = vec4(lightingResult, 1.0);
}
