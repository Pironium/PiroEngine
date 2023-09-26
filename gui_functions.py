# gui_functions.py

class PiroGUI:
    def __init__(self):
        self.objects = []  # Список 3D-объектов в игре

    def create_cube(self, size, position):
        """
        Создает 3D-куб в игре.

        :param size: Размер куба (ширина, высота, глубина)
        :param position: Положение куба в трехмерном пространстве (x, y, z)
        """
        cube = {
            'type': 'cube',
            'size': size,
            'position': position
        }
        self.objects.append(cube)

    def create_sphere(self, radius, position):
        """
        Создает 3D-сферу в игре.

        :param radius: Радиус сферы
        :param position: Положение сферы в трехмерном пространстве (x, y, z)
        """
        sphere = {
            'type': 'sphere',
            'radius': radius,
            'position': position
        }
        self.objects.append(sphere)

    def translate_object(self, obj_index, new_position):
        """
        Перемещает 3D-объект по новым координатам.

        :param obj_index: Индекс объекта в списке self.objects
        :param new_position: Новое положение объекта в трехмерном пространстве (x, y, z)
        """
        if 0 <= obj_index < len(self.objects):
            self.objects[obj_index]['position'] = new_position

    def delete_object(self, obj_index):
        """
        Удаляет 3D-объект из игры.

        :param obj_index: Индекс объекта в списке self.objects
        """
        if 0 <= obj_index < len(self.objects):
            del self.objects[obj_index]

# Пример использования:
if __name__ == "__main__":
    gui = PiroGUI()
    gui.create_cube((2, 2, 2), (0, 0, 0))
    gui.create_sphere(1, (3, 3, 3))
    gui.translate_object(0, (1, 1, 1))
    gui.delete_object(1)
