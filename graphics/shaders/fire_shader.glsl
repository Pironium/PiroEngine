// Fire Shader
#version 330 core
out vec4 FragColor;

uniform sampler2D texture_diffuse1;
uniform float time;

void main()
{
    vec2 uv = gl_FragCoord.xy / 1920.0; // Assuming a 1920x1080 resolution

    // Create a realistic fire effect using Perlin noise
    float noise = texture(texture_diffuse1, uv).r;
    noise += sin(uv.y * 10.0 + time) * 0.1;
    noise += sin(uv.x * 20.0 + time) * 0.05;

    vec3 fireColor = vec3(1.0, 0.5, 0.0); // Orange-red color

    // Adjust the color based on the noise
    vec3 finalColor = fireColor * noise;

    FragColor = vec4(finalColor, 1.0);
}
