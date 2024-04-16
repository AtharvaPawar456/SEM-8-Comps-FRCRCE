import socket

class StatefulFileClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.host, self.port))

            while True:
                # Get user input
                user_input = input("> ")

                # Send user input to server
                sock.sendall(user_input.encode())

                # Receive and print response from server
                response = sock.recv(1024).decode()
                print(response)

if __name__ == "__main__":
    client = StatefulFileClient('localhost', 12345)
    client.run()