# pip install rpyc

import rpyc

class MyService(rpyc.Service):
    def on_connect(self, conn):
        print("Client connected")

    def on_disconnect(self, conn):
        print("Client disconnected")

    def exposed_add_numbers(self, x, y):
        return x + y

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer

    # Start the RMI server
    t = ThreadedServer(MyService, port=8000)
    print("RMI Server is listening on port 8000...")
    t.start()
