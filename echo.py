# listen on port 8080, print the received message and send it back to the sender.
import socket
import time

# listening port number
PORT = 8080

# echo sending port number
PORT_ECHO = 8081

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
sock.bind(('', PORT))

print(f"Listening on port {PORT}")
print(f"Echoing on port {PORT_ECHO}")

while True:
    # Receive the message
    data, addr = sock.recvfrom(1024)

    # Print the received message
    try:
        print(f"Received message from {addr} : {data.decode()}")
    except UnicodeDecodeError:
        print(f"Received binary data message from {addr} : {data.hex() }")

    # Send the message back to the sender
    sock.sendto(data, (addr[0], addr[1]))

    # Wait for 1 second before receiving the next message
    time.sleep(0.1)
    