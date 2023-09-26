# piroengine_3d.py

class PiroEngine3D:
    def __init__(self):
        self.scenes = []  # Хранение списка 3D сцен
        self.active_scene = None  # Активная 3D сцена

    def create_scene(self, name):
        """
        Создать новую 3D сцену.
        :param name: Название сцены.
        """
        scene = Scene3D(name)
        self.scenes.append(scene)

    def set_active_scene(self, scene_name):
        """
        Установить активную 3D сцену.
        :param scene_name: Название сцены.
        """
        for scene in self.scenes:
            if scene.name == scene_name:
                self.active_scene = scene
                break

    def add_3d_object(self, object):
        """
        Добавить 3D объект в активную сцену.
        :param object: 3D объект для добавления.
        """
        if self.active_scene is not None:
            self.active_scene.add_object(object)
        else:
            raise Exception("Активная 3D сцена не установлена.")

class Scene3D:
    def __init__(self, name):
        self.name = name
        self.objects = []  # Список 3D объектов в сцене

    def add_object(self, object):
        """
        Добавить 3D объект в сцену.
        :param object: 3D объект для добавления.
        """
        self.objects.append(object)

class GameObject3D:
    def __init__(self, name):
        self.name = name
        self.position = (0, 0, 0)
        self.scale = (1, 1, 1)
        self.rotation = (0, 0, 0)

    def translate(self, x, y, z):
        """
        Переместить объект в 3D пространстве.
        :param x: Перемещение по оси X.
        :param y: Перемещение по оси Y.
        :param z: Перемещение по оси Z.
        """
        self.position = (self.position[0] + x, self.position[1] + y, self.position[2] + z)

    def scale_up(self, factor):
        """
        Увеличить объект в масштабе.
        :param factor: Множитель масштаба.
        """
        self.scale = (self.scale[0] * factor, self.scale[1] * factor, self.scale[2] * factor)

    def rotate(self, x, y, z):
        """
        Повернуть объект в 3D пространстве.
        :param x: Угол поворота по оси X.
        :param y: Угол поворота по оси Y.
        :param z: Угол поворота по оси Z.
        """
        self.rotation = (self.rotation[0] + x, self.rotation[1] + y, self.rotation[2] + z)
