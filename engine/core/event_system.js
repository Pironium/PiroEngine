class EventSystem {
  constructor() {
    this.eventListeners = new Map();
  }

  subscribe(eventType, callback) {
    if (!this.eventListeners.has(eventType)) {
      this.eventListeners.set(eventType, []);
    }
    this.eventListeners.get(eventType).push(callback);
  }

  unsubscribe(eventType, callback) {
    if (this.eventListeners.has(eventType)) {
      const listeners = this.eventListeners.get(eventType);
      const index = listeners.indexOf(callback);
      if (index !== -1) {
        listeners.splice(index, 1);
      }
    }
  }

  publish(eventType, eventData) {
    if (this.eventListeners.has(eventType)) {
      const listeners = this.eventListeners.get(eventType);
      for (const listener of listeners) {
        // Use asynchronous execution for better parallelism
        setTimeout(() => {
          listener(eventData);
        }, 0);
      }
    }
  }
}
