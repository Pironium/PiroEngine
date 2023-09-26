class ReactiveEnvironment:
    def __init__(self):
        self.objects = []
        self.environment_data = {}

    def add_object(self, obj):
        self.objects.append(obj)

    def remove_object(self, obj):
        self.objects.remove(obj)

    def update_environment(self):
        for obj in self.objects:
            obj.react_to_environment(self.environment_data)

class GameObject:
    def __init__(self, name):
        self.name = name

    def react_to_environment(self, environment_data):
        pass  # В этом методе можно реализовать логику взаимодействия объекта с окружением
