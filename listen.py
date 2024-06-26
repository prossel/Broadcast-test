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
    try:
        print(f"Received message from {addr} : {data.decode()}")
    except UnicodeDecodeError:
        print(f"Received binary data message from {addr} : {data.hex() }")

    print(addr)

    # Wait for 1 second before receiving the next message
    time.sleep(1)
    