# PiroEngine - Particle Generator

class ParticleGenerator:
    def __init__(self):
        self.particles = []

    def create_particle(self, position, color, size, velocity):
        particle = {
            'position': position,
            'color': color,
            'size': size,
            'velocity': velocity
        }
        self.particles.append(particle)

    def update_particles(self, delta_time):
        for particle in self.particles:
            # Update particle position based on velocity
            particle['position'][0] += particle['velocity'][0] * delta_time
            particle['position'][1] += particle['velocity'][1] * delta_time
            particle['position'][2] += particle['velocity'][2] * delta_time

    def render_particles(self):
        for particle in self.particles:
            # Render each particle as a 3D object with specified color and size
            render_3d_particle(particle['position'], particle['color'], particle['size'])

    def clear_particles(self):
        self.particles = []

# Function to render a 3D particle - Implement this in your game rendering engine
def render_3d_particle(position, color, size):
    # Code to render a 3D particle with given properties
    pass
