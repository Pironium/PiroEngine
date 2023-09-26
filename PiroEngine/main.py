# PiroEngine - New Game Engine
# Copyright (c) 2023 Pironium Inc.

class PiroEngine:
    def __init__(self):
        self.scenes = []
        self.current_scene = None

    def add_scene(self, scene):
        self.scenes.append(scene)

    def set_scene(self, scene_name):
        for scene in self.scenes:
            if scene.name == scene_name:
                self.current_scene = scene
                break

    def update(self):
        if self.current_scene:
            self.current_scene.update()

class Scene:
    def __init__(self, name):
        self.name = name

    def update(self):
        pass
