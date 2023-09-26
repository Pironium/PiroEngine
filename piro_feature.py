# (путь к файлу)/piro_feature.py

import random

class PiroFeature:
    def __init__(self, game_engine):
        self.game_engine = game_engine

    def generate_random_level(self, difficulty):
        if difficulty < 1 or difficulty > 10:
            raise ValueError("Difficulty level must be between 1 and 10.")
        
        level = []
        for _ in range(10 * difficulty):
            row = []
            for _ in range(20 * difficulty):
                cell_type = random.choice(["wall", "enemy", "treasure", "empty"])
                row.append(cell_type)
            level.append(row)
        
        return level

    def add_random_level_to_game(self, game_name, difficulty):
        game = self.game_engine.get_game(game_name)
        if game is None:
            raise ValueError("Game not found.")

        random_level = self.generate_random_level(difficulty)
        game.add_level(random_level)
