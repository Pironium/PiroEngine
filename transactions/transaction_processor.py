class TransactionProcessor:
    def __init__(self):
        self.transactions = []

    def process_transaction(self, user_id, amount, description):
        # Добавляем новую транзакцию в список
        transaction = {
            'user_id': user_id,
            'amount': amount,
            'description': description,
            'timestamp': get_current_timestamp()
        }
        self.transactions.append(transaction)

    def get_user_balance(self, user_id):
        # Вычисляем баланс пользователя на основе транзакций
        user_balance = 0
        for transaction in self.transactions:
            if transaction['user_id'] == user_id:
                user_balance += transaction['amount']
        return user_balance

    def get_transactions_by_user(self, user_id):
        # Возвращаем список транзакций пользователя
        user_transactions = []
        for transaction in self.transactions:
            if transaction['user_id'] == user_id:
                user_transactions.append(transaction)
        return user_transactions

    def get_recent_transactions(self, limit=10):
        # Возвращаем 'limit' последних транзакций
        sorted_transactions = sorted(self.transactions, key=lambda x: x['timestamp'], reverse=True)
        return sorted_transactions[:limit]

def get_current_timestamp():
    # Генерируем текущий временной штамп
    # (Здесь используется фича, имитирующая 3D движок - точное время)
    import time
    return int(time.time())
