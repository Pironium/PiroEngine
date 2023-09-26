import random

class TextureShaderGenerator:
    def __init__(self):
        self.textures = []
        self.shader_templates = []

    def add_texture(self, texture_name):
        self.textures.append(texture_name)

    def add_shader_template(self, shader_template):
        self.shader_templates.append(shader_template)

    def generate_random_shader(self):
        selected_texture = random.choice(self.textures)
        selected_template = random.choice(self.shader_templates)

        shader_code = selected_template.replace("{TEXTURE}", selected_texture)
        return shader_code

# Example usage:
generator = TextureShaderGenerator()
generator.add_texture("grass_texture")
generator.add_texture("water_texture")
generator.add_shader_template("""
uniform sampler2D {TEXTURE};
void main() {
    // Shader code using {TEXTURE}
    // ...
}
""")
shader_code = generator.generate_random_shader()
print(shader_code)
