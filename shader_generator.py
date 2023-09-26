# Python code for shader generation in PiroEngine

import random

class ShaderGenerator:
    def __init__(self):
        self.shader_templates = [
            "void main() { gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0); }",
            "void main() { gl_FragColor = vec4(0.0, 1.0, 0.0, 1.0); }",
            "void main() { gl_FragColor = vec4(0.0, 0.0, 1.0, 1.0); }",
            # Добавьте здесь еще множество других шаблонов шейдеров
        ]

    def generate_shader(self):
        # Выбираем случайный шаблон шейдера
        shader_template = random.choice(self.shader_templates)
        return shader_template

# Пример использования
if __name__ == "__main__":
    shader_generator = ShaderGenerator()
    generated_shader = shader_generator.generate_shader()
    print(generated_shader)
