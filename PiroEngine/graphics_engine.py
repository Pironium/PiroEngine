class PiroGraphicsEngine:
    def __init__(self):
        self.render_pipeline = []
        self.models = []
        self.lights = []

    def add_model(self, model):
        """
        Добавляет 3D-модель в сцену.
        :param model: 3D-модель для добавления.
        """
        self.models.append(model)

    def add_light(self, light):
        """
        Добавляет источник света в сцену.
        :param light: Источник света для добавления.
        """
        self.lights.append(light)

    def render_scene(self):
        """
        Рендерит 3D-сцену с учетом всех моделей и источников света в рендер-пайплайне.
        """
        for model in self.models:
            model.transform()
            model.render()

        for light in self.lights:
            light.illuminate()

        for item in self.render_pipeline:
            item.render()

class Piro3DModel:
    def __init__(self, mesh):
        self.mesh = mesh

    def transform(self):
        """
        Производит преобразования 3D-модели перед рендерингом.
        """
        pass

    def render(self):
        """
        Рендерит 3D-модель на сцене.
        """
        pass

class PiroLight:
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def illuminate(self):
        """
        Освещает сцену с использованием источника света.
        """
        pass
