import os

def compile_game_for_windows(game_folder):
    # Compile game for Windows
    os.system('compile_command_for_windows')

def compile_game_for_android(game_folder):
    # Compile game for Android
    os.system('compile_command_for_android')

def compile_game_for_iphone(game_folder):
    # Compile game for iPhone
    os.system('compile_command_for_iphone')

def compile_game_for_macos(game_folder):
    # Compile game for macOS
    os.system('compile_command_for_macos')

def compile_game_for_linux(game_folder):
    # Compile game for Linux
    os.system('compile_command_for_linux')

def compile_game_for_ps4(game_folder):
    # Compile game for PS4
    os.system('compile_command_for_ps4')

def compile_game_for_xbox_one(game_folder):
    # Compile game for Xbox One
    os.system('compile_command_for_xbox_one')

if __name__ == "__main__":
    game_folder = "path_to_game_folder"
    
    compile_game_for_windows(game_folder)
    compile_game_for_android(game_folder)
    compile_game_for_iphone(game_folder)
    compile_game_for_macos(game_folder)
    compile_game_for_linux(game_folder)
    compile_game_for_ps4(game_folder)
    compile_game_for_xbox_one(game_folder)
