import socket
import random

# Create a TCP/IP socket using UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
sock.bind(server_address)

while True:
    
    data, address = sock.recvfrom(4096)
    if data:
        n = random.randint(0,10)
        # If n >= 3, convert data to upper case and send to client.
        if(n >= 3):
            sent = sock.sendto(data.upper(), address)