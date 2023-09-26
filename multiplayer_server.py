import socket
import threading

class MultiplayerServer:
    def __init__(self, port):
        self.port = port
        self.clients = []
        self.server_socket = None
        self.is_running = False

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(("0.0.0.0", self.port))
        self.server_socket.listen(5)
        self.is_running = True
        print(f"Multiplayer server is running on port {self.port}")

        while self.is_running:
            client_socket, client_address = self.server_socket.accept()
            print(f"New connection from {client_address}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()
            self.clients.append((client_socket, client_address))

    def stop(self):
        self.is_running = False
        self.server_socket.close()

    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    break

                # Handle multiplayer game logic here
                # You can implement your unique features for the PiroEngine

                for client in self.clients:
                    if client[0] != client_socket:
                        client[0].send(data)

            except Exception as e:
                print(f"Error: {e}")
                break

    def broadcast(self, message):
        for client in self.clients:
            client[0].send(message.encode())

if __name__ == "__main__":
    server = MultiplayerServer(8080)
    server.start()
