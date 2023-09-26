class GameObject:
    def __init__(self, name, position=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1)):
        self.name = name
        self.position = position
        self.rotation = rotation
        self.scale = scale

    def move(self, x, y, z):
        self.position = (self.position[0] + x, self.position[1] + y, self.position[2] + z)

    def rotate(self, x, y, z):
        self.rotation = (self.rotation[0] + x, self.rotation[1] + y, self.rotation[2] + z)

    def scale_up(self, factor):
        self.scale = (self.scale[0] * factor, self.scale[1] * factor, self.scale[2] * factor)

    def scale_down(self, factor):
        self.scale = (self.scale[0] / factor, self.scale[1] / factor, self.scale[2] / factor)


class SceneManager:
    def __init__(self):
        self.scene_objects = []

    def add_object(self, game_object):
        self.scene_objects.append(game_object)

    def remove_object(self, game_object):
        if game_object in self.scene_objects:
            self.scene_objects.remove(game_object)

    def clear_scene(self):
        self.scene_objects = []

    def get_objects_by_name(self, name):
        return [obj for obj in self.scene_objects if obj.name == name]
