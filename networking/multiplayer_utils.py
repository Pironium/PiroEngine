# PiroEngine Multiplayer Utilities

class MultiplayerManager:
    def __init__(self):
        self.players = {}  # Словарь для хранения информации о подключенных игроках

    def connect_player(self, player_id, player_name):
        """
        Подключить игрока к серверу мультиплеера.

        :param player_id: Уникальный идентификатор игрока
        :param player_name: Имя игрока
        """
        if player_id not in self.players:
            self.players[player_id] = {'name': player_name, 'status': 'connected'}
        else:
            print(f"Player with ID {player_id} is already connected.")

    def disconnect_player(self, player_id):
        """
        Отключить игрока от сервера мультиплеера.

        :param player_id: Уникальный идентификатор игрока
        """
        if player_id in self.players:
            self.players[player_id]['status'] = 'disconnected'
        else:
            print(f"Player with ID {player_id} is not connected.")

    def get_connected_players(self):
        """
        Получить список подключенных игроков.

        :return: Список подключенных игроков
        """
        connected_players = [player['name'] for player in self.players.values() if player['status'] == 'connected']
        return connected_players

    def send_game_state(self, player_id, game_state):
        """
        Отправить состояние игры конкретному игроку.

        :param player_id: Уникальный идентификатор игрока
        :param game_state: Состояние игры для отправки
        """
        if player_id in self.players:
            # Отправляем игровое состояние игроку с использованием сетевого протокола
            print(f"Sending game state to player {self.players[player_id]['name']}: {game_state}")
        else:
            print(f"Player with ID {player_id} is not connected.")
