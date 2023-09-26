# main.py

class PiroEngine:
    def __init__(self):
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)

    def remove_entity(self, entity):
        self.entities.remove(entity)

class Entity:
    def __init__(self, name):
        self.name = name

    def update(self):
        pass

    def render(self):
        pass

class Renderer:
    def __init__(self):
        self.render_queue = []

    def add_to_render_queue(self, entity):
        self.render_queue.append(entity)

    def render_all(self):
        for entity in self.render_queue:
            entity.render()

class PhysicsSystem:
    def __init__(self):
        pass

    def update(self, entities):
        for entity in entities:
            entity.update()

class PiroScript:
    def __init__(self):
        pass

    def execute(self, script):
        pass
