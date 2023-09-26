# advanced_3d_feature.py

class Advanced3DFeature:
    def __init__(self):
        self.enabled = False
        self.objects = []

    def enable_feature(self):
        self.enabled = True

    def disable_feature(self):
        self.enabled = False

    def add_object(self, obj):
        if self.enabled:
            self.objects.append(obj)
            print(f"Added object: {obj}")

    def remove_object(self, obj):
        if self.enabled and obj in self.objects:
            self.objects.remove(obj)
            print(f"Removed object: {obj}")

    def render_scene(self):
        if self.enabled:
            print("Rendering advanced 3D scene:")
            for obj in self.objects:
                obj.render()

class GameObject:
    def __init__(self, name):
        self.name = name

    def render(self):
        print(f"Rendering {self.name}")

# Example usage:
if __name__ == "__main__":
    engine = Advanced3DFeature()
    engine.enable_feature()

    object1 = GameObject("Object1")
    object2 = GameObject("Object2")

    engine.add_object(object1)
    engine.add_object(object2)

    engine.render_scene()

    engine.remove_object(object1)
    engine.render_scene()
