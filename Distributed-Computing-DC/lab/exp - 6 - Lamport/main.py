from multiprocessing import Process, Pipe
from os import getpid
from datetime import datetime

# Helper function to print the local Lamport timestamp and the actual time on the machine
def local_time(counter):
    return ' (LAMPORT_TIME={}, LOCAL_TIME={})'.format(counter, datetime.now())

# Function to send a message and update the Lamport clock
def send_message(pipe, pid, counter, msg='Empty shell'):
    counter += 1
    pipe.send((msg, counter))
    print('Tx msg from ' + str(pid) + "\t\t" + local_time(counter) + "\tTx-MSG : " + msg)
    return counter

# Function to receive a message and update the Lamport clock
def recv_message(pipe, pid, counter):
    message, timestamp = pipe.recv()
    counter = max(counter, timestamp) + 1
    print('Rx msg at ' + str(pid) + "\t\t\t" + local_time(counter) + '\tRx-MSG : ' + message + "\n")
    return counter

# Function to simulate the process behavior
def process_function(pipe, msg, counter=0):
    pid = getpid()
    # Example of sending a message
    counter = send_message(pipe, pid, counter, msg)
    # Example of receiving a message
    counter = recv_message(pipe, pid, counter)

if __name__ == "__main__":
    print("System Started !!!\n")
    parent_conn, child_conn = Pipe()
    
    print("P1 init ...")
    p1 = Process(target=process_function, args=(child_conn, "p1", 0))
    
    print("P2 init ...")
    p2 = Process(target=process_function, args=(parent_conn, "p2", 0))


    parent_conn2, child_conn2 = Pipe()
    p3 = Process(target=process_function, args=(child_conn2, "p3", 10))
    print("P3 init ...")

    p4 = Process(target=process_function, args=(parent_conn2, "p4", 20))
    print("P4 init ...")

    print("\n\n")


    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()


'''
### Output on terminal:

System Started !!!

P1 init ...
P2 init ...
P3 init ...
P4 init ...



Tx msg from 10547                (LAMPORT_TIME=1, LOCAL_TIME=2024-03-20 20:33:48.044170)        Tx-MSG : p1
Rx msg at 10547                  (LAMPORT_TIME=2, LOCAL_TIME=2024-03-20 20:33:48.044494)        Rx-MSG : p2

Tx msg from 10548                (LAMPORT_TIME=1, LOCAL_TIME=2024-03-20 20:33:48.044490)        Tx-MSG : p2
Rx msg at 10548                  (LAMPORT_TIME=2, LOCAL_TIME=2024-03-20 20:33:48.044573)        Rx-MSG : p1

Tx msg from 10549                (LAMPORT_TIME=11, LOCAL_TIME=2024-03-20 20:33:48.044901)       Tx-MSG : p3
Rx msg at 10549                  (LAMPORT_TIME=22, LOCAL_TIME=2024-03-20 20:33:48.045158)       Rx-MSG : p4

Tx msg from 10550                (LAMPORT_TIME=21, LOCAL_TIME=2024-03-20 20:33:48.045156)       Tx-MSG : p4
Rx msg at 10550                  (LAMPORT_TIME=22, LOCAL_TIME=2024-03-20 20:33:48.045218)       Rx-MSG : p3
'''