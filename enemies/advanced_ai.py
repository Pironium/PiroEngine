# advanced_ai.py - Улучшенный ИИ для врагов

import random

class AdvancedAI:
    def __init__(self):
        self.health = 100
        self.damage = 10
        self.strategy = "aggressive"

    def decide_action(self, player_position):
        # Адаптация к действиям игрока
        if player_position == "hidden":
            self.strategy = "wait_and_seek"
        elif player_position == "visible":
            self.strategy = "attack"

        # Выбор действия на основе стратегии
        if self.strategy == "aggressive":
            return self.attack()
        elif self.strategy == "wait_and_seek":
            return self.wait_and_seek()
        elif self.strategy == "attack":
            return self.attack()

    def attack(self):
        # Алгоритм атаки
        print("Enemy is attacking!")
        return self.damage

    def wait_and_seek(self):
        # Алгоритм ожидания и поиска игрока
        print("Enemy is waiting and seeking!")
        return None

if __name__ == "__main__":
    enemy = AdvancedAI()
    player_position = random.choice(["hidden", "visible"])
    print(f"Player is {player_position}")
    enemy.decide_action(player_position)
