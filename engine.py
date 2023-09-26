# engine.py

class PiroEngine:
    def __init__(self):
        self.platforms = []

    def add_platform(self, platform):
        self.platforms.append(platform)

    def compile_games(self):
        for platform in self.platforms:
            platform.compile_game()

class Platform:
    def __init__(self, name):
        self.name = name

    def compile_game(self):
        print(f"Compiling games for {self.name} platform")

class WindowsPlatform(Platform):
    def compile_game(self):
        print("Compiling games for Windows")

class AndroidPlatform(Platform):
    def compile_game(self):
        print("Compiling games for Android")

class iPhonePlatform(Platform):
    def compile_game(self):
        print("Compiling games for iPhone")

class MacOSPlatform(Platform):
    def compile_game(self):
        print("Compiling games for macOS")

class LinuxPlatform(Platform):
    def compile_game(self):
        print("Compiling games for Linux")

class PS4Platform(Platform):
    def compile_game(self):
        print("Compiling games for PS4")

class XboxOnePlatform(Platform):
    def compile_game(self):
        print("Compiling games for Xbox One")
