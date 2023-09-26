class PiroEngine:
    def __init__(self):
        self.scene = Scene()

    def start(self):
        self.scene.initialize()
        self.scene.run()

class Scene:
    def __init__(self):
        self.objects = []

    def initialize(self):
        # Добавим инициализацию сцены здесь
        pass

    def run(self):
        # Цикл обновления и рендеринга сцены
        pass
