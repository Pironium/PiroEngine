# interact_with_environment.py

class InteractiveObject:
    def __init__(self, name):
        self.name = name
        self.is_lit = False

    def interact_with_light(self):
        if not self.is_lit:
            print(f"{self.name} is now interacting with the environment and capturing light.")
            self.is_lit = True
        else:
            print(f"{self.name} is already capturing light.")

class PiroEngine:
    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        if isinstance(obj, InteractiveObject):
            self.objects.append(obj)
        else:
            print("Can only add InteractiveObjects to the PiroEngine.")

    def simulate_environment_interaction(self):
        for obj in self.objects:
            obj.interact_with_light()

# Example usage:

if __name__ == "__main__":
    engine = PiroEngine()

    object1 = InteractiveObject("Lantern")
    object2 = InteractiveObject("Mirror")

    engine.add_object(object1)
    engine.add_object(object2)

    engine.simulate_environment_interaction()
