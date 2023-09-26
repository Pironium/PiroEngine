class VideoEditor:
    def __init__(self):
        self.scenes = []
        self.current_scene = None

    def add_scene(self, scene):
        self.scenes.append(scene)

    def set_current_scene(self, scene):
        self.current_scene = scene

    def render_video(self):
        video_frames = []
        for scene in self.scenes:
            video_frames.extend(scene.render())
        return video_frames


class Scene:
    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def render(self):
        video_frames = []
        for obj in self.objects:
            video_frames.extend(obj.render())
        return video_frames


class VideoObject:
    def __init__(self):
        self.frames = []

    def add_frame(self, frame):
        self.frames.append(frame)

    def render(self):
        return self.frames


class MovieMaker:
    def __init__(self):
        self.video_editor = VideoEditor()

    def create_video(self):
        # Create scenes and objects, add frames
        scene1 = Scene()
        object1 = VideoObject()
        object1.add_frame("Frame 1 of object 1")
        object1.add_frame("Frame 2 of object 1")
        scene1.add_object(object1)
        self.video_editor.add_scene(scene1)

        scene2 = Scene()
        object2 = VideoObject()
        object2.add_frame("Frame 1 of object 2")
        object2.add_frame("Frame 2 of object 2")
        scene2.add_object(object2)
        self.video_editor.add_scene(scene2)

        # Set the current scene and render the video
        self.video_editor.set_current_scene(scene1)
        video_frames = self.video_editor.render_video()
        return video_frames
