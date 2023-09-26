import socket

class ConnectionManager:
    def __init__(self, server_address, port):
        self.server_address = server_address
        self.port = port
        self.socket = None

    def connect(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.server_address, self.port))
            print("Connected to the server.")
        except Exception as e:
            print(f"Error connecting to the server: {str(e)}")

    def send_data(self, data):
        try:
            if self.socket:
                self.socket.sendall(data.encode())
                print(f"Sent data: {data}")
            else:
                print("Connection not established.")
        except Exception as e:
            print(f"Error sending data: {str(e)}")

    def receive_data(self):
        try:
            if self.socket:
                data = self.socket.recv(1024).decode()
                print(f"Received data: {data}")
                return data
            else:
                print("Connection not established.")
                return None
        except Exception as e:
            print(f"Error receiving data: {str(e)}")
            return None

    def disconnect(self):
        try:
            if self.socket:
                self.socket.close()
                print("Disconnected from the server.")
            else:
                print("Connection not established.")
        except Exception as e:
            print(f"Error disconnecting: {str(e)}")

if __name__ == "__main__":
    # Example usage of the ConnectionManager class
    connection_manager = ConnectionManager("example.com", 12345)
    connection_manager.connect()
    connection_manager.send_data("Hello, server!")
    response = connection_manager.receive_data()
    connection_manager.disconnect()
