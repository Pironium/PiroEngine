import random

class PiroEngine:
    def __init__(self):
        self.games = []

    def add_game(self, game_name):
        self.games.append(game_name)

    def generateRandomGameName(self):
        adjectives = ['Epic', 'Fantastic', 'Mystical', 'Incredible', 'Legendary']
        nouns = ['Adventure', 'Quest', 'Maze', 'Kingdom', 'Journey']
        return random.choice(adjectives) + ' ' + random.choice(nouns)

if __name__ == "__main__":
    engine = PiroEngine()
    for _ in range(10):
        game_name = engine.generateRandomGameName()
        engine.add_game(game_name)
        print(f"Created game: {game_name}")
