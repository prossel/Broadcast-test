import socket
import time

# Set the port number
PORT = 8080

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
sock.bind(('', PORT))

while True:
    # Receive the message
    data, addr = sock.recvfrom(1024)

    # Print the received message
    print(f"Received message: {data.decode()}")

    # Wait for 1 second before receiving the next message
    time.sleep(1)
    