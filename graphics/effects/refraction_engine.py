# PiroEngine Refraction Engine

class RefractionEngine:
    def __init__(self):
        self.active_objects = []
    
    def add_refractive_object(self, obj):
        self.active_objects.append(obj)
    
    def remove_refractive_object(self, obj):
        if obj in self.active_objects:
            self.active_objects.remove(obj)
    
    def update_refraction(self):
        for obj in self.active_objects:
            obj.apply_refraction()
