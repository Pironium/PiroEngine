class BoundingBox:
    def __init__(self, min_point, max_point):
        self.min_point = min_point
        self.max_point = max_point

class BVHNode:
    def __init__(self, objects, bounding_box):
        self.objects = objects
        self.bounding_box = bounding_box
        self.left = None
        self.right = None

def build_bvh_tree(objects):
    # Рекурсивно строим BVH-дерево
    if len(objects) == 1:
        return BVHNode(objects[0], objects[0].calculate_bounding_box())
    elif len(objects) == 0:
        return None

    # Выбираем ось разбиения
    split_axis = longest_axis(objects)

    # Сортируем объекты по центру их ограничивающих объемов
    objects.sort(key=lambda x: x.calculate_bounding_box().center()[split_axis])

    # Разбиваем объекты на две группы
    left_objects = objects[:len(objects) // 2]
    right_objects = objects[len(objects) // 2:]

    left_node = build_bvh_tree(left_objects)
    right_node = build_bvh_tree(right_objects)

    bounding_box = BoundingBox(
        min(left_node.bounding_box.min_point, right_node.bounding_box.min_point),
        max(left_node.bounding_box.max_point, right_node.bounding_box.max_point)
    )

    node = BVHNode(None, bounding_box)
    node.left = left_node
    node.right = right_node

    return node

def longest_axis(objects):
    # Выбираем ось разбиения, основываясь на самой длинной стороне ограничивающего объема
    min_point = objects[0].calculate_bounding_box().min_point
    max_point = objects[0].calculate_bounding_box().max_point
    for obj in objects:
        min_point = min(min_point, obj.calculate_bounding_box().min_point)
        max_point = max(max_point, obj.calculate_bounding_box().max_point)

    axis_lengths = [max_point[0] - min_point[0], max_point[1] - min_point[1], max_point[2] - min_point[2]]
    return axis_lengths.index(max(axis_lengths))

class CollisionObject:
    def __init__(self, geometry):
        self.geometry = geometry

    def calculate_bounding_box(self):
        # Рассчитываем ограничивающий объем для объекта
        # (например, AABB - Axis-Aligned Bounding Box)
        # Возвращаем BoundingBox
        pass

def detect_collisions(root_node, ray):
    # Рекурсивно обходим BVH-дерево и проверяем коллизии с объектами
    pass
