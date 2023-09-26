// Liquid Shader
#version 330 core

in vec2 TexCoord;
out vec4 FragColor;

uniform sampler2D texture;
uniform float time;

void main()
{
    // Определяем центр для эффекта жидкости
    vec2 center = vec2(0.5, 0.5);

    // Вычисляем расстояние от текущей точки до центра
    float distance = length(TexCoord - center);

    // Создаем волны на основе времени
    float wave = sin(distance * 10.0 - time * 2.0) * 0.1;

    // Получаем цвет из текстуры и искажаем его с помощью волны
    vec4 textureColor = texture(texture, TexCoord + wave);

    // Выводим искаженный цвет
    FragColor = textureColor;
}
