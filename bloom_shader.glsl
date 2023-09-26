// Этот шейдер реализует эффект блюра (блума) для улучшения графики игр.
// Он будет работать с высокой точностью и эффективно использовать GPU.

#version 330 core

uniform sampler2D sceneTexture;
uniform sampler2D brightPassTexture;

in vec2 TexCoords;

out vec4 FragColor;

const float kernelSize = 15.0;
const float sigma = 5.0;

void main()
{
    vec3 col = vec3(0.0);
    vec2 texelSize = 1.0 / textureSize(sceneTexture, 0);

    for (float x = -kernelSize; x <= kernelSize; x++)
    {
        for (float y = -kernelSize; y <= kernelSize; y++)
        {
            float offset = sqrt(x * x + y * y);
            float weight = exp(-(offset * offset) / (2.0 * sigma * sigma)) / (2.0 * 3.14159265 * sigma * sigma);

            col += texture(sceneTexture, TexCoords + vec2(x, y) * texelSize).rgb * weight;
        }
    }

    FragColor = vec4(col, 1.0) + texture(brightPassTexture, TexCoords);
}
