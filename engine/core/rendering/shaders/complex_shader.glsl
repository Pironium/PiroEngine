// Complex Shader with Fractal Geometry
#version 330 core

uniform float time;
in vec2 fragCoord;

out vec4 FragColor;

void main()
{
    vec2 p = (2.0 * fragCoord - 1.0) * vec2(1.6, 1.2);
    vec2 z = p;
    float intensity = 0.0;
    
    for(int i = 0; i < 300; i++)
    {
        z = vec2(z.x * z.x - z.y * z.y, 2.0 * z.x * z.y) + p;
        intensity += length(z);
    }
    
    intensity = log(intensity + 1.0) / log(300.0);
    
    vec3 color = vec3(0.5 + 0.5 * cos(3.0 + intensity + time),
                      0.5 + 0.5 * sin(5.0 + intensity + time),
                      0.5 + 0.5 * cos(7.0 + intensity + time));
    
    FragColor = vec4(color, 1.0);
}
