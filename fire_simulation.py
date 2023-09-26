# Fire Simulation Function for PiroEngine

import random

class FireSimulation:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.fire_pixels = [[0 for _ in range(width)] for _ in range(height)]

    def initialize_fire(self):
        for x in range(self.width):
            self.fire_pixels[self.height - 1][x] = random.randint(1, 36)

    def spread_fire(self):
        for y in range(self.height - 1):
            for x in range(self.width):
                decay = random.randint(1, 4)
                target_x = x - decay + 1
                if target_x < 0:
                    target_x = 0
                elif target_x >= self.width:
                    target_x = self.width - 1

                self.fire_pixels[y][x] = max(0, self.fire_pixels[y + 1][target_x] - decay)

    def render_frame(self):
        for y in range(self.height):
            for x in range(self.width):
                intensity = self.fire_pixels[y][x]
                # Render the fire intensity as a color in the frame (e.g., RGB values)
                # Display the pixel at (x, y) with the calculated color
                pixel_color = calculate_color(intensity)
                display_pixel(x, y, pixel_color)

    def calculate_color(self, intensity):
        # Implement a color mapping based on the fire intensity
        # Return the RGB color value

    def display_pixel(self, x, y, color):
        # Display the pixel at coordinates (x, y) with the given color


# Example usage:
if __name__ == "__main__":
    engine = PiroEngine()
    simulation = FireSimulation(engine.width, engine.height)
    simulation.initialize_fire()

    while True:
        simulation.spread_fire()
        simulation.render_frame()
        engine.update_display()
