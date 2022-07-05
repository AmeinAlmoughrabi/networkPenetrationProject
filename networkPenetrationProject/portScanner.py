# 

# This is a port scanner that will allow us find open ports in any host
# We will be using the threading module to run multiple threads at the same time

# The reason we are interested in open ports is for the purpose of security 
# It is ocnsidered a security gap to have open ports on your network

# Port scanning works by using sockets to connect to a target at a specific port
# If the port is open, the connection will be successful
# If the port is closed, the connection will be unsuccessful

# The port scan method will be as follows:
    # 1. Create a socket object
    # 2. Connect to the target at the port specified
    # 3. Close the socket
    # 4. If the connection was successful, the port is open
    # 5. If the connection was unsuccessful, the port is closed


import threading
import socket
from queue import Queue

target = ""
    # if you want to test it on your own computer, you can change the target to your own ip address
    # you can use local host at 127.0.0.1, but do not do this to others as it is highly illegal


# This will be for the multithreading part of the code
# Starting by defining an empty queue and list of ports

queue = Queue()
openPorts = []



def portScanner(port):
    try:
        # We are going to try to connect by creating a socket object as an internet socket (INET) and a stream socket (STREAM) (TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        # if there are no errors we can basically return true assuming it would not get to this point if it was not successful
        print("Port {}: Open".format(port))
        s.close()
    except:
        print("Port {}: Closed".format(port))


for port in range(1, 1024):
    # these are the standardized ports reserved for HTTP, FTP, SSH, etc.
    portScanner(port)
    # this is the function that will be run in multiple threads

# Now if we just run multiple threads, we can potentially scan the same port multiple times
# We are going to use queues to prevent this

def fillQueue(port_list):
    for port in port_list:
        queue.put(port)
    # this will fill the queue with the ports we want to scan
    # this will add the port to the queue
    # since queue is a FIFO, it will add the port to the end of the queue

# now to define a worker method that will run in multiple threads
def worker():
    while not queue.empty():
        port = queue.get()
        if portScanner(port):
            print( "Port {}: Open".format(port))
            openPorts.append(port)
    # this will run the portScanner function for each port in the queue

port_list = range(1, 1024)
fillQueue(port_list)
# this will fill the queue with the ports we want to scan

# now to define an empty thread list
threadList = []

for thread in range(10):
    t = threading.Thread(target=worker)
    threadList.append(t)
    t.start()
    # this will start 10 threads
    # this will run the worker function for each thread

for thread in threadList:
    thread.start()
    # this will start the threads


for thread in threadList:
    thread.join()
    # this will wait for all the threads to finish

print ("Open ports: {}".format(openPorts))
# this will print the open ports
# We want this to prin after al the ports are done

