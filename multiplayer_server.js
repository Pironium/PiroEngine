// PiroEngine Multiplayer Server
// This module handles multiplayer game server functionality.

const WebSocket = require('ws');

class MultiplayerServer {
  constructor(port) {
    this.port = port;
    this.clients = new Set();
    this.server = null;
  }

  start() {
    this.server = new WebSocket.Server({ port: this.port });

    this.server.on('connection', (socket) => {
      this.clients.add(socket);
      console.log('New client connected');

      socket.on('message', (message) => {
        console.log(`Received message: ${message}`);

        // Handle game logic and broadcast messages to other clients
        this.broadcast(message, socket);
      });

      socket.on('close', () => {
        this.clients.delete(socket);
        console.log('Client disconnected');
      });
    });

    console.log(`Multiplayer server started on port ${this.port}`);
  }

  broadcast(message, sender) {
    this.clients.forEach((client) => {
      if (client !== sender && client.readyState === WebSocket.OPEN) {
        client.send(message);
      }
    });
  }

  stop() {
    this.server.close(() => {
      console.log('Multiplayer server stopped');
    });
  }
}

module.exports = MultiplayerServer;
