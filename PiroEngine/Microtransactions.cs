using System;

namespace PiroEngine
{
    public class Microtransactions
    {
        private Dictionary<string, decimal> userBalances = new Dictionary<string, decimal>();
        private Dictionary<string, List<Transaction>> transactionHistory = new Dictionary<string, List<Transaction>>();

        public void InitializeUserBalance(string userId, decimal initialBalance)
        {
            if (!userBalances.ContainsKey(userId))
            {
                userBalances[userId] = initialBalance;
                transactionHistory[userId] = new List<Transaction>();
            }
        }

        public decimal GetUserBalance(string userId)
        {
            if (userBalances.ContainsKey(userId))
            {
                return userBalances[userId];
            }
            else
            {
                throw new ArgumentException("User does not exist.");
            }
        }

        public void PurchaseItem(string userId, string itemId, decimal itemPrice)
        {
            if (userBalances.ContainsKey(userId))
            {
                if (userBalances[userId] >= itemPrice)
                {
                    userBalances[userId] -= itemPrice;
                    Transaction transaction = new Transaction(userId, itemId, itemPrice, DateTime.Now);
                    transactionHistory[userId].Add(transaction);
                }
                else
                {
                    throw new InvalidOperationException("Insufficient funds.");
                }
            }
            else
            {
                throw new ArgumentException("User does not exist.");
            }
        }

        public List<Transaction> GetTransactionHistory(string userId)
        {
            if (transactionHistory.ContainsKey(userId))
            {
                return transactionHistory[userId];
            }
            else
            {
                throw new ArgumentException("User does not exist.");
            }
        }

        public class Transaction
        {
            public string UserId { get; }
            public string ItemId { get; }
            public decimal Amount { get; }
            public DateTime Timestamp { get; }

            public Transaction(string userId, string itemId, decimal amount, DateTime timestamp)
            {
                UserId = userId;
                ItemId = itemId;
                Amount = amount;
                Timestamp = timestamp;
            }
        }
    }
}
