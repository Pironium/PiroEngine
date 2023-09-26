#version 330 core

layout(location = 0) out vec4 gbufferPosition;
layout(location = 1) out vec4 gbufferNormal;
layout(location = 2) out vec4 gbufferAlbedo;
layout(location = 3) out vec4 gbufferSpecular;

uniform sampler2D depthTexture;
uniform sampler2D normalTexture;
uniform sampler2D albedoTexture;
uniform sampler2D specularTexture;

in vec2 TexCoords;

void main()
{
    vec4 depthSample = texture(depthTexture, TexCoords);
    float depth = depthSample.x;
    
    vec3 normal = texture(normalTexture, TexCoords).xyz;
    vec3 albedo = texture(albedoTexture, TexCoords).xyz;
    vec3 specular = texture(specularTexture, TexCoords).xyz;
    
    // Custom deferred shading algorithm goes here...
    
    gbufferPosition = vec4(vec3(0.0), 1.0);
    gbufferNormal = vec4(vec3(0.0), 1.0);
    gbufferAlbedo = vec4(vec3(0.0), 1.0);
    gbufferSpecular = vec4(vec3(0.0), 1.0);
}
