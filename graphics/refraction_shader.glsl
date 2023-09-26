// Vertex shader
#version 330 core
layout(location = 0) in vec3 inPosition;
layout(location = 1) in vec2 inTexCoord;
out vec2 TexCoord;
uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main()
{
    TexCoord = inTexCoord;
    gl_Position = projection * view * model * vec4(inPosition, 1.0);
}

// Fragment shader
#version 330 core
in vec2 TexCoord;
out vec4 FragColor;
uniform sampler2D screenTexture;
uniform sampler2D refractionTexture;
uniform float refractionFactor;

void main()
{
    vec2 distortedTexCoord = TexCoord + (texture(refractionTexture, TexCoord).xy - 0.5) * refractionFactor;
    FragColor = texture(screenTexture, distortedTexCoord);
}
