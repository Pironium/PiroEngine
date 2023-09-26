class PiroGraphics3D:
    def __init__(self, resolution=(1920, 1080), shaders=None):
        self.resolution = resolution
        self.shaders = shaders if shaders else []
        self.vertex_buffers = []
        self.models = []
    
    def add_model(self, model):
        self.models.append(model)
    
    def compile_shaders(self):
        # Compiles shaders and links them to the graphics pipeline
        pass
    
    def render_frame(self):
        # Renders a frame with the current scene and shaders
        pass

# Example usage:
graphics = PiroGraphics3D(resolution=(1920, 1080), shaders=['phong_shader', 'bloom_shader'])
graphics.add_model('model1.obj')
graphics.add_model('model2.obj')
graphics.compile_shaders()
graphics.render_frame()
