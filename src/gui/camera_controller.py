# Import necessary libraries
import pygame
from piroengine import PiroEngine

class CameraController:
    def __init__(self, engine: PiroEngine):
        self.engine = engine
        self.cameras = []

    def create_camera(self, name, x, y, z, rotation_x, rotation_y, rotation_z):
        camera = self.engine.create_camera(name)
        camera.set_position(x, y, z)
        camera.set_rotation(rotation_x, rotation_y, rotation_z)
        self.cameras.append(camera)

    def switch_camera(self, camera_name):
        for camera in self.cameras:
            if camera.name == camera_name:
                self.engine.set_active_camera(camera)
                break

    def update(self):
        # Handle camera controls here, e.g., camera movement and rotation based on user input.
        pass

# Initialize the GUI camera controller
if __name__ == "__main__":
    engine = PiroEngine()
    engine.init()

    camera_controller = CameraController(engine)

    # Create cameras with initial positions and rotations
    camera_controller.create_camera("MainCamera", 0, 0, 0, 0, 0, 0)
    camera_controller.create_camera("Camera2", 1, 2, -3, 0, 0, 0)
    camera_controller.create_camera("Camera3", -2, 0, 4, 45, 30, 0)

    # Set the active camera
    camera_controller.switch_camera("MainCamera")

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the camera controller
        camera_controller.update()

        # Render the scene
        engine.render()

    engine.quit()
