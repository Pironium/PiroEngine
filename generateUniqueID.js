// PiroEngine - Unique ID Generator

class UniqueIDGenerator {
  constructor() {
    this.usedIDs = new Set();
  }

  generate() {
    let id;
    do {
      id = this.generateRandomID();
    } while (this.usedIDs.has(id));

    this.usedIDs.add(id);
    return id;
  }

  generateRandomID() {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    const length = 10;
    let id = '';
    for (let i = 0; i < length; i++) {
      const randomIndex = Math.floor(Math.random() * characters.length);
      id += characters.charAt(randomIndex);
    }
    return id;
  }
}

module.exports = UniqueIDGenerator;
