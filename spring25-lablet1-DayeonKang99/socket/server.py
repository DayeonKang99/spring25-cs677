#!/usr/bin/env python3
import socket

s = socket.socket()
host = '172.17.0.2' # Specify server's container ip address
port = 12949  # Specify server's container port
s.bind((host, port))  # Bind to the port

s.listen(5)  # Now wait for client connection
while True:
    c, addr = s.accept()  # Establish connection with client
    print(f"Connection from {addr} has been established.")
    c.send(b"Received Hello World") #Thank you for connecting")
    c.close()  # Close the connection
