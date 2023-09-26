class RoomManager {
  constructor() {
    this.rooms = new Map();
  }

  // Создать новую игровую комнату
  createRoom(roomName, maxPlayers) {
    if (this.rooms.has(roomName)) {
      throw new Error('Room with the same name already exists.');
    }

    const room = {
      name: roomName,
      maxPlayers: maxPlayers,
      players: [],
    };

    this.rooms.set(roomName, room);
    return room;
  }

  // Присоединить игрока к комнате
  joinRoom(roomName, player) {
    const room = this.rooms.get(roomName);
    if (!room) {
      throw new Error('Room not found.');
    }

    if (room.players.length >= room.maxPlayers) {
      throw new Error('Room is full.');
    }

    room.players.push(player);
  }

  // Получить список игроков в комнате
  getPlayersInRoom(roomName) {
    const room = this.rooms.get(roomName);
    if (!room) {
      throw new Error('Room not found.');
    }

    return room.players;
  }

  // Запустить игровую сессию в комнате
  startGameInRoom(roomName) {
    const room = this.rooms.get(roomName);
    if (!room) {
      throw new Error('Room not found.');
    }

    // Здесь можно добавить логику для запуска игры в комнате
    // Например, начать синхронизацию игрового состояния между игроками
  }
}

module.exports = RoomManager;
