class MultiplayerManager {
  constructor() {
    this.players = [];
  }

  addPlayer(player) {
    this.players.push(player);
  }

  removePlayer(player) {
    const index = this.players.indexOf(player);
    if (index !== -1) {
      this.players.splice(index, 1);
    }
  }

  broadcastMessage(message) {
    this.players.forEach(player => {
      player.receiveMessage(message);
    });
  }
}

module.exports = MultiplayerManager;
