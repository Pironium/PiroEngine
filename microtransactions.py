# microtransactions.py

# Import necessary modules
import datetime

# Define a class for managing microtransactions
class MicroTransactionManager:
    def __init__(self):
        self.transactions = []

    def process_transaction(self, user_id, item_id, amount_paid):
        # Simulate a transaction and add it to the list
        timestamp = datetime.datetime.now()
        transaction_data = {
            "user_id": user_id,
            "item_id": item_id,
            "amount_paid": amount_paid,
            "timestamp": timestamp
        }
        self.transactions.append(transaction_data)

    def get_user_transactions(self, user_id):
        # Retrieve all transactions for a specific user
        user_transactions = [t for t in self.transactions if t["user_id"] == user_id]
        return user_transactions

    def calculate_user_spending(self, user_id):
        # Calculate the total spending of a user
        user_transactions = self.get_user_transactions(user_id)
        total_spending = sum(t["amount_paid"] for t in user_transactions)
        return total_spending

# Define a class for managing in-game items available for purchase
class InGameItemManager:
    def __init__(self):
        self.available_items = {}

    def add_item(self, item_id, item_name, price):
        # Add an item to the list of available items
        self.available_items[item_id] = {"name": item_name, "price": price}

    def get_item_price(self, item_id):
        # Retrieve the price of a specific in-game item
        item = self.available_items.get(item_id)
        if item:
            return item["price"]
        else:
            return None

# Example usage
if __name__ == "__main__":
    transaction_manager = MicroTransactionManager()
    item_manager = InGameItemManager()

    # Add some in-game items
    item_manager.add_item("item1", "Health Potion", 5)
    item_manager.add_item("item2", "Sword of Power", 10)
    item_manager.add_item("item3", "Magic Shield", 7)

    # Simulate transactions
    transaction_manager.process_transaction("user1", "item1", 5)
    transaction_manager.process_transaction("user1", "item2", 10)
    transaction_manager.process_transaction("user2", "item1", 5)

    # Calculate user spending
    user1_spending = transaction_manager.calculate_user_spending("user1")
    user2_spending = transaction_manager.calculate_user_spending("user2")

    print(f"User1 total spending: ${user1_spending}")
    print(f"User2 total spending: ${user2_spending}")
