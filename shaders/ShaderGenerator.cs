using System;

public class ShaderGenerator
{
    private Random random;

    public ShaderGenerator()
    {
        random = new Random();
    }

    public string GenerateVertexShader()
    {
        // Генерируем сложный вершинный шейдер
        string vertexShader = @"
            #version 330 core

            layout(location = 0) in vec3 inPosition;
            layout(location = 1) in vec2 inTexCoord;

            uniform mat4 model;
            uniform mat4 view;
            uniform mat4 projection;

            out vec2 texCoord;

            void main()
            {
                gl_Position = projection * view * model * vec4(inPosition, 1.0);
                texCoord = inTexCoord;
            }
        ";

        return vertexShader;
    }

    public string GenerateFragmentShader()
    {
        // Генерируем сложный фрагментный шейдер
        string fragmentShader = @"
            #version 330 core

            in vec2 texCoord;

            uniform sampler2D texture;

            out vec4 fragColor;

            void main()
            {
                fragColor = texture(texture, texCoord);
            }
        ";

        return fragmentShader;
    }
}
