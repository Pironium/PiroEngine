class PiroEngine:
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def remove_component(self, component):
        self.components.remove(component)

    def update(self):
        for component in self.components:
            component.update()

class GameComponent:
    def __init__(self, name):
        self.name = name

    def update(self):
        print(f"Updating {self.name} component")

# Новая функция в новом файле
def new_engine_function():
    print("This is a new function in the PiroEngine")

if __name__ == "__main__":
    engine = PiroEngine()

    component1 = GameComponent("Component 1")
    component2 = GameComponent("Component 2")

    engine.add_component(component1)
    engine.add_component(component2)

    engine.update()

    # Использование новой функции
    new_engine_function()
