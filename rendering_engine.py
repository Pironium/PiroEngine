import numpy as np
import OpenGL.GL as gl

class PiroRenderer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.init_rendering()

    def init_rendering(self):
        # Initialize OpenGL
        gl.glClearColor(0.0, 0.0, 0.0, 1.0)
        gl.glViewport(0, 0, self.width, self.height)

        # Create a vertex buffer
        vertices = np.array([
            -0.5, -0.5, 0.0,
             0.5, -0.5, 0.0,
             0.0,  0.5, 0.0
        ], dtype=np.float32)

        self.vao = gl.glGenVertexArrays(1)
        gl.glBindVertexArray(self.vao)

        self.vbo = gl.glGenBuffers(1)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vbo)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, vertices.nbytes, vertices, gl.GL_STATIC_DRAW)

        gl.glEnableVertexAttribArray(0)
        gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, gl.GL_FALSE, 0, None)

    def render(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glBindVertexArray(self.vao)
        gl.glDrawArrays(gl.GL_TRIANGLES, 0, 3)

    def resize(self, width, height):
        self.width = width
        self.height = height
        gl.glViewport(0, 0, self.width, self.height)

    def cleanup(self):
        gl.glDeleteVertexArrays(1, [self.vao])
        gl.glDeleteBuffers(1, [self.vbo])

if __name__ == "__main__":
    # Example usage
    import glfw

    # Initialize GLFW
    if not glfw.init():
        exit()

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(800, 600, "PiroEngine", None, None)
    if not window:
        glfw.terminate()
        exit()

    # Make the window's context current
    glfw.make_context_current(window)

    renderer = PiroRenderer(800, 600)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        renderer.render()
        glfw.swap_buffers(window)

    renderer.cleanup()
    glfw.terminate()
