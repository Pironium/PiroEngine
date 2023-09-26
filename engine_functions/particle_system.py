class ParticleSystem:
    def __init__(self):
        self.particles = []

    def add_particle(self, particle):
        self.particles.append(particle)

    def update(self, delta_time):
        for particle in self.particles:
            particle.update(delta_time)

class Particle:
    def __init__(self, x, y, velocity):
        self.x = x
        self.y = y
        self.velocity = velocity

    def update(self, delta_time):
        self.x += self.velocity * delta_time
        self.y += self.velocity * delta_time

    def render(self):
        # Code to render the particle on the screen
        pass
