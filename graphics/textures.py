# Import necessary libraries
import os
import pygame

# Define a class for managing textures
class TextureManager:
    def __init__(self):
        self.textures = {}  # Dictionary to store loaded textures

    def load_texture(self, filename):
        # Check if the texture is already loaded
        if filename in self.textures:
            return self.textures[filename]

        # Generate a unique texture ID
        texture_id = hash(filename)

        # Load the texture from file
        try:
            texture = pygame.image.load(os.path.join("textures", filename))
            self.textures[filename] = (texture_id, texture)
            return texture_id
        except pygame.error as e:
            print(f"Failed to load texture '{filename}': {str(e)}")
            return None

    def get_texture(self, texture_id):
        # Get the texture associated with the given ID
        for filename, (id, texture) in self.textures.items():
            if id == texture_id:
                return texture

# Example usage
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    texture_manager = TextureManager()

    # Load textures
    player_texture_id = texture_manager.load_texture("player.png")
    background_texture_id = texture_manager.load_texture("background.jpg")

    # Render textures
    player_texture = texture_manager.get_texture(player_texture_id)
    background_texture = texture_manager.get_texture(background_texture_id)

    # Blit textures onto the screen
    screen.blit(background_texture, (0, 0))
    screen.blit(player_texture, (400, 300))

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
