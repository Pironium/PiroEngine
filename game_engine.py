class PiroEngine:
    def __init__(self):
        self.games = []

    def create_game(self, game_name):
        new_game = {"name": game_name, "status": "initialized"}
        self.games.append(new_game)

    def start_game(self, game_name):
        for game in self.games:
            if game["name"] == game_name:
                game["status"] = "running"

    def stop_game(self, game_name):
        for game in self.games:
            if game["name"] == game_name:
                game["status"] = "stopped"

    def list_running_games(self):
        running_games = [game["name"] for game in self.games if game["status"] == "running"]
        return running_games

    def list_initialized_games(self):
        initialized_games = [game["name"] for game in self.games if game["status"] == "initialized"]
        return initialized_games
