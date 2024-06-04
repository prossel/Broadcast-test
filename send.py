# broadcast a message to an IP address

import socket
import time

# Set the broadcast address
address = '255.255.255.255'

# Set the port number
PORT = 8080

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enable broadcasting mode
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Set the broadcast address and port
sock.bind(('', PORT))

while True:
    # Send the message
    message = "Hello, world!"
    sock.sendto(message.encode(), (address, PORT))

    # Wait for 1 second before sending the message again
    time.sleep(1)