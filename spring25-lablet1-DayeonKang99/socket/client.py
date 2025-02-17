#!/usr/bin/env python3
import socket

s = socket.socket()
host = '172.17.0.2' # Specify server's container ip address
port = 12949  # Specify server's container port

s.connect((host, port))
print(s.recv(1024))
s.send(b"Hello World")
s.close()  # Close the socket when done
