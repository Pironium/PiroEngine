# animation_controller.py

class AnimationController:
    def __init__(self):
        self.animations = {}

    def add_animation(self, object_id, animation):
        if object_id not in self.animations:
            self.animations[object_id] = []
        self.animations[object_id].append(animation)

    def play_animation(self, object_id, animation_name):
        if object_id in self.animations and animation_name in self.animations[object_id]:
            # Здесь бы был сложный код для воспроизведения анимации
            print(f"Playing animation '{animation_name}' for object '{object_id}'")
        else:
            print(f"Animation '{animation_name}' not found for object '{object_id}'")

    def stop_animation(self, object_id, animation_name):
        if object_id in self.animations and animation_name in self.animations[object_id]:
            # Здесь бы был сложный код для остановки анимации
            print(f"Stopping animation '{animation_name}' for object '{object_id}'")
        else:
            print(f"Animation '{animation_name}' not found for object '{object_id}'")

# Дополнительные сложные функции и классы могут идти здесь

if __name__ == "__main__":
    # Пример использования AnimationController
    controller = AnimationController()
    controller.add_animation("character1", "walk")
    controller.add_animation("character1", "jump")
    controller.play_animation("character1", "walk")
    controller.stop_animation("character1", "jump")
