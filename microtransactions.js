// microtransactions.js - PiroEngine Microtransactions System

class Microtransactions {
  constructor() {
    this.transactions = [];
  }

  // Function to initiate a microtransaction
  initiateTransaction(userId, itemId, itemPrice) {
    const transactionId = this.generateTransactionId();
    const transaction = {
      id: transactionId,
      userId: userId,
      itemId: itemId,
      itemPrice: itemPrice,
      status: 'pending',
    };

    this.transactions.push(transaction);
    return transactionId;
  }

  // Function to complete a microtransaction
  completeTransaction(transactionId) {
    const transactionIndex = this.findTransactionIndex(transactionId);
    if (transactionIndex !== -1) {
      this.transactions[transactionIndex].status = 'completed';
      return true;
    }
    return false;
  }

  // Function to cancel a microtransaction
  cancelTransaction(transactionId) {
    const transactionIndex = this.findTransactionIndex(transactionId);
    if (transactionIndex !== -1) {
      this.transactions[transactionIndex].status = 'canceled';
      return true;
    }
    return false;
  }

  // Function to retrieve the status of a microtransaction
  getTransactionStatus(transactionId) {
    const transactionIndex = this.findTransactionIndex(transactionId);
    if (transactionIndex !== -1) {
      return this.transactions[transactionIndex].status;
    }
    return 'not_found';
  }

  // Generate a unique transaction ID
  generateTransactionId() {
    return 'txn_' + Math.random().toString(36).substr(2, 9);
  }

  // Find the index of a transaction by its ID
  findTransactionIndex(transactionId) {
    return this.transactions.findIndex((transaction) => transaction.id === transactionId);
  }
}

module.exports = Microtransactions;
