class PiroEngine:
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def remove_component(self, component):
        self.components.remove(component)

    def update(self, delta_time):
        for component in self.components:
            component.update(delta_time)

class PiroComponent:
    def __init__(self):
        self.data = []

    def update(self, delta_time):
        # Your unique component logic goes here
        pass
