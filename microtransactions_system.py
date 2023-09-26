class MicrotransactionsSystem:
    def __init__(self):
        self.wallets = {}  # Словарь для хранения балансов пользователей

    def create_wallet(self, user_id):
        # Создаем кошелек для пользователя
        if user_id not in self.wallets:
            self.wallets[user_id] = 0

    def deposit(self, user_id, amount):
        # Пополнение баланса пользователя
        if user_id in self.wallets and amount > 0:
            self.wallets[user_id] += amount

    def withdraw(self, user_id, amount):
        # Списание с баланса пользователя
        if user_id in self.wallets and amount > 0 and self.wallets[user_id] >= amount:
            self.wallets[user_id] -= amount
            return True
        return False

    def get_balance(self, user_id):
        # Получение баланса пользователя
        if user_id in self.wallets:
            return self.wallets[user_id]
        return 0

    def purchase_item(self, user_id, item_id, item_cost):
        # Покупка предмета
        if user_id in self.wallets and self.wallets[user_id] >= item_cost:
            if self.withdraw(user_id, item_cost):
                # Выполняем действия по покупке предмета
                # Например, активируем предмет в игре
                return True
        return False
