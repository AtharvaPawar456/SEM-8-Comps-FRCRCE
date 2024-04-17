# Code 1:

# -------------------------------------------------
# Single Threading
# -------------------------------------------------


# Client.py

# https://notepad.pw/uM3KJmWHJDwga695XKFo

import socket

def client_program():
    host = socket.gethostname() # as both code is running on same pc
    port = 5000 # socket server port number
    client_socket = socket.socket() # instantiate
    client_socket.connect((host, port)) # connect to the server
    message = input(" -> ") # take input
    while message.lower().strip() != 'bye':
        client_socket.send(message.encode()) # send message
        data = client_socket.recv(1024).decode() # receive response
        print('Received from server: ' + data) # show in terminal
        message = input(" -> ") # again take input
    client_socket.close() # close the connection

if __name__ == '__main__':
    client_program()


# Server.py
import socket

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000 # initiate port no above 1024
    server_socket = socket.socket() # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port)) # bind host address and port together
    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept() # accept new connection
    print("Connection from: " + str(address))

    while True:
        # receive data stream. It won’t accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
        # if data is not received break
            break
        
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode()) # send data to the client
        
    conn.close() # close the connection
    
if __name__ == '__main__':
    server_program()



# Code 2:


# -------------------------------------------------
# Multi Threading
# -------------------------------------------------

# Client1.py

import socket
host = socket.gethostname()

port = 2004
BUFFER_SIZE = 2000
MESSAGE = input("tcpClientA: Enter message/ Enter exit:")
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientA.connect((host, port))

while MESSAGE != 'exit':
    tcpClientA.send(MESSAGE.encode())
    data = tcpClientA.recv(BUFFER_SIZE).decode()
    print (" Client2 received data:", data)
    MESSAGE = input("tcpClientA: Enter message to continue/ Enter exit:")

tcpClientA.close()

# -------------------------------------------------

# Client2.py
import socket

host = socket.gethostname()
port = 2004
BUFFER_SIZE = 2000
MESSAGE = input("tcpClientB: Enter message/ Enter exit:")
tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientB.connect((host, port))

while MESSAGE != 'exit':
    tcpClientB.send(MESSAGE.encode())
    data = tcpClientB.recv(BUFFER_SIZE).decode()
    print (" Client received data:", data)
    MESSAGE = input("tcpClientB: Enter message to continue/ Enter exit:")

tcpClientB.close()

# -------------------------------------------------

import socket
from threading import Thread
from socketserver import ThreadingMixIn

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread):
    
    def __init__(self,ip,port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print ("[+] New server socket thread started for " + ip + ":" + str(port))

    def run(self):
        while True :
            data = conn.recv(2048).decode()
            print ("Server received data:", data)
            MESSAGE = input("Multithreaded Python server : Enter Response from Server/Enter exit:")
            if MESSAGE == 'exit':
                break
            conn.send(MESSAGE.encode()) # echo

# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = '0.0.0.0'
TCP_PORT = 2004
BUFFER_SIZE = 20 # Usually 1024, but we need quick response
tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpServer.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpServer.listen(4)
    print ("Multithreaded Python server : Waiting for connections from TCP clients...")
    (conn, (ip,port)) = tcpServer.accept()
    newthread = ClientThread(ip,port)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()	