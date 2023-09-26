# PiroEngine Sound Manager

class SoundManager:
    def __init__(self):
        self.sound_library = {}  # Dictionary to store loaded sound assets
        self.current_sound = None  # Currently playing sound

    def load_sound(self, sound_id, file_path):
        """
        Load a sound asset from file.
        :param sound_id: Unique identifier for the sound.
        :param file_path: Path to the sound file.
        """
        if sound_id not in self.sound_library:
            # Load and initialize the sound resource
            sound = Sound(file_path)
            self.sound_library[sound_id] = sound
            print(f"Loaded sound '{sound_id}' from {file_path}")
        else:
            print(f"Sound '{sound_id}' is already loaded.")

    def play_sound(self, sound_id):
        """
        Play a loaded sound.
        :param sound_id: Unique identifier for the sound.
        """
        if sound_id in self.sound_library:
            if self.current_sound is not None:
                self.current_sound.stop()  # Stop the currently playing sound if any
            sound = self.sound_library[sound_id]
            sound.play()
            self.current_sound = sound
            print(f"Playing sound '{sound_id}'")
        else:
            print(f"Sound '{sound_id}' is not loaded.")

    def stop_sound(self):
        """
        Stop the currently playing sound.
        """
        if self.current_sound is not None:
            self.current_sound.stop()
            self.current_sound = None
            print("Stopped the currently playing sound.")

class Sound:
    def __init__(self, file_path):
        self.file_path = file_path

    def play(self):
        """
        Simulate playing the sound.
        """
        print(f"Playing sound from {self.file_path}")

    def stop(self):
        """
        Simulate stopping the sound.
        """
        print("Stopped sound")

# Initialize the SoundManager
sound_manager = SoundManager()
