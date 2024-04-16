import socket
import threading
import os

class FileSystem:
    def __init__(self, root_path):
        self.root_path = root_path

    def create_file(self, path):
        full_path = os.path.join(self.root_path, path)
        with open(full_path, 'w') as f:
            f.write('')
        return "File created successfully"

    def read_file(self, path):
        full_path = os.path.join(self.root_path, path)
        with open(full_path, 'r') as f:
            content = f.read()
        return content

    def write_file(self, path, content):
        full_path = os.path.join(self.root_path, path)
        with open(full_path, 'w') as f:
            f.write(content)
        return "File written successfully"

    def delete_file(self, path):
        full_path = os.path.join(self.root_path, path)
        os.remove(full_path)
        return "File deleted successfully"

class StatefulFileServer:
    def __init__(self, host, port, file_system):
        self.host = host
        self.port = port
        self.file_system = file_system
        self.sessions = {}

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((self.host, self.port))
            sock.listen()

            while True:
                conn, addr = sock.accept()
                client_thread = threading.Thread(target=self.handle_client, args=(conn, addr))
                client_thread.start()

    def handle_client(self, conn, addr):
        addr_1 = input("Enter portNumber: ")
        client_id = addr[0] + ":" + addr_1
        print("Client: %s" % client_id)
        session_data = self.sessions.get(client_id, {})
        print(f"Stored data for client {client_id}: {session_data}")
        # Parse client request and perform file system operation
        request = conn.recv(1024).decode()
        response = self.handle_request(request, session_data)

        # Send response to client
        conn.sendall(response.encode())

        # Update session data
        self.sessions[client_id] = session_data

        conn.close()

    def handle_request(self, request, session_data):
        tokens = request.split()
        command = tokens[0]
        session_data[command] = tokens[1]

        if command == "CREATE":
            path = tokens[1]
            return self.file_system.create_file(path)

        elif command == "READ":
            path = tokens[1]
            return self.file_system.read_file(path)

        elif command == "WRITE":
            path = tokens[1]
            content = ' '.join(tokens[2:])
            return self.file_system.write_file(path, content)

        elif command == "DELETE":
            path = tokens[1]
            return self.file_system.delete_file(path)

        else:
            return "Unknown command"

if __name__ == "__main__":
    file_system = FileSystem('./filesystem')
    server = StatefulFileServer('localhost', 12345, file_system)
    server.run()