// PiroEngine Microtransaction System

class MicrotransactionSystem {
  constructor() {
    this.transactions = [];
  }

  // Generate a unique transaction ID
  generateTransactionID() {
    const timestamp = Date.now();
    const random = Math.floor(Math.random() * 1000);
    return `${timestamp}-${random}`;
  }

  // Initialize a new transaction
  initTransaction(itemName, itemPrice, currencyType) {
    const transactionID = this.generateTransactionID();
    const transaction = {
      id: transactionID,
      itemName,
      itemPrice,
      currencyType,
      status: 'pending',
    };
    this.transactions.push(transaction);
    return transactionID;
  }

  // Process a transaction
  processTransaction(transactionID, onSuccess, onError) {
    const transaction = this.transactions.find((t) => t.id === transactionID);
    if (!transaction) {
      onError('Transaction not found');
      return;
    }

    // Simulate payment processing delay
    setTimeout(() => {
      // Simulate successful transaction with a 90% success rate
      const successProbability = Math.random();
      if (successProbability < 0.9) {
        transaction.status = 'completed';
        onSuccess('Transaction completed successfully');
      } else {
        transaction.status = 'failed';
        onError('Transaction failed');
      }
    }, 2000); // 2 seconds delay
  }

  // Get the status of a transaction
  getTransactionStatus(transactionID) {
    const transaction = this.transactions.find((t) => t.id === transactionID);
    if (!transaction) {
      return 'Transaction not found';
    }
    return transaction.status;
  }
}

module.exports = MicrotransactionSystem;
