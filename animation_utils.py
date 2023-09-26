# Импортируем необходимые библиотеки
import math
import time

class AnimationController:
    def __init__(self, object_to_animate):
        self.object_to_animate = object_to_animate
        self.keyframes = []
        self.current_frame = 0
        self.playing = False

    def add_keyframe(self, position, rotation, scale, time_stamp):
        keyframe = {
            'position': position,
            'rotation': rotation,
            'scale': scale,
            'time_stamp': time_stamp
        }
        self.keyframes.append(keyframe)

    def play_animation(self):
        if not self.keyframes:
            print("No keyframes added. Cannot play animation.")
            return

        self.playing = True
        start_time = time.time()
        while self.playing:
            elapsed_time = time.time() - start_time
            if self.current_frame < len(self.keyframes) - 1:
                if elapsed_time >= self.keyframes[self.current_frame + 1]['time_stamp']:
                    self.current_frame += 1

                alpha = (elapsed_time - self.keyframes[self.current_frame]['time_stamp']) / \
                        (self.keyframes[self.current_frame + 1]['time_stamp'] - self.keyframes[self.current_frame]['time_stamp'])

                position = self.interpolate(self.keyframes[self.current_frame]['position'],
                                             self.keyframes[self.current_frame + 1]['position'], alpha)
                rotation = self.interpolate(self.keyframes[self.current_frame]['rotation'],
                                             self.keyframes[self.current_frame + 1]['rotation'], alpha)
                scale = self.interpolate(self.keyframes[self.current_frame]['scale'],
                                          self.keyframes[self.current_frame + 1]['scale'], alpha)

                self.object_to_animate.set_transform(position, rotation, scale)
            else:
                self.playing = False

    def stop_animation(self):
        self.playing = False

    def interpolate(self, start_value, end_value, alpha):
        return start_value + (end_value - start_value) * alpha

# Пример использования класса AnimationController:
# animated_object = GameObject()
# animation_controller = AnimationController(animated_object)
# animation_controller.add_keyframe(Vector3(0, 0, 0), Quaternion(0, 0, 0, 1), Vector3(1, 1, 1), 0)
# animation_controller.add_keyframe(Vector3(10, 5, 0), Quaternion(0, math.pi, 0, 1), Vector3(2, 2, 2), 5)
# animation_controller.play_animation()
