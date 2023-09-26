# PiroEngine Movie Maker Module

class MovieMaker:
    def __init__(self):
        self.scenes = []

    def add_scene(self, scene):
        """
        Add a scene to the movie.
        
        Args:
            scene (Scene): The scene to add.
        """
        self.scenes.append(scene)

    def export_movie(self, filename):
        """
        Export the movie to a file.
        
        Args:
            filename (str): The name of the output movie file.
        """
        with open(filename, 'w') as f:
            # Write movie metadata
            f.write("PiroEngine Movie Maker Output\n")
            f.write("Version: 1.0\n\n")

            # Write each scene
            for i, scene in enumerate(self.scenes):
                f.write(f"Scene {i + 1}:\n")
                f.write(f"Duration: {scene.duration} seconds\n")

                # Write scene content
                for item in scene.content:
                    if isinstance(item, str):
                        f.write(f"Text: {item}\n")
                    elif isinstance(item, Image):
                        f.write(f"Image: {item.filename}\n")

                f.write("\n")

class Scene:
    def __init__(self, duration):
        self.duration = duration
        self.content = []

    def add_text(self, text):
        """
        Add text to the scene.
        
        Args:
            text (str): The text to add.
        """
        self.content.append(text)

    def add_image(self, image):
        """
        Add an image to the scene.
        
        Args:
            image (Image): The image to add.
        """
        self.content.append(image)

class Image:
    def __init__(self, filename):
        self.filename = filename
