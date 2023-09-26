// water.fx - Водный эффект для PiroEngine

// Vertex Shader
#version 330 core
layout(location = 0) in vec3 inPosition;
layout(location = 1) in vec2 inTexCoord;

out vec2 texCoord;

uniform mat4 projection;
uniform mat4 view;
uniform mat4 model;

void main()
{
    texCoord = inTexCoord;
    gl_Position = projection * view * model * vec4(inPosition, 1.0);
}

// Fragment Shader
#version 330 core
in vec2 texCoord;
out vec4 fragColor;

uniform sampler2D reflectionTexture;
uniform sampler2D refractionTexture;
uniform sampler2D dudvMap;
uniform sampler2D normalMap;

uniform vec3 cameraPosition;

const float waveSpeed = 0.03;
const float waveStrength = 0.02;

void main()
{
    vec2 distortedTexCoord = texCoord + texture(dudvMap, texCoord).rg * 2.0 - 1.0;
    vec2 refractedTexCoord = refract(vec3(0.0, 0.0, -1.0), normalize(vec3(distortedTexCoord.x, distortedTexCoord.y, 1.0)), 0.1);

    vec4 reflectionColor = texture(reflectionTexture, vec2(texCoord.x, texCoord.y));
    vec4 refractionColor = texture(refractionTexture, refractedTexCoord);

    vec3 normal = texture(normalMap, texCoord).rgb * 2.0 - 1.0;
    vec3 viewDirection = normalize(cameraPosition - vec3(gl_FragCoord.xy, 0.0));
    float specular = pow(max(dot(normal, viewDirection), 0.0), 32.0);

    float time = waveSpeed * float(gl_GlobalInvocationID.x);
    float waveOffset = sin(time) * waveStrength;
    vec2 distortedRefractedTexCoord = refractedTexCoord + vec2(waveOffset, waveOffset);

    vec4 finalColor = mix(reflectionColor, refractionColor, 0.5) + vec4(specular);
    fragColor = finalColor;
}
