// Visual Effects Shader
#version 330 core

uniform sampler2D texture; // Входная текстура

in vec2 TexCoord; // Текстурная координата из вершинного шейдера
out vec4 FragColor; // Выходной цветной пиксель

void main()
{
    vec4 texColor = texture2D(texture, TexCoord);

    // Пример: Применение сепия-эффекта
    vec3 sepiaColor = vec3(0.393, 0.769, 0.189);
    FragColor = vec4(vec3(dot(texColor.rgb, sepiaColor)), texColor.a);
}
