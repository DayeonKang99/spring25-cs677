# Socket Programming in Python

## How to Run

First, start a docker container by running the below command in the lablet 1 directory 
```
$ ./cs677-run-docker
```

Before running the server and the client, you need to specify the server's IP and port in `server.py` and `client.py.` 

Specifically, update Line 5 and Line 6 in `client.py`, and Line 5 and Line 6 in `server.py` to set the server's IP and port to the Docker container's IP and exposed port. 

Now, start the server by running:
```
$ python3 server.py
```

Then, start the client in a separate terminal:
```
$ python3 client.py
```

## References

[1] Tutorials at https://www.tutorialspoint.com/python_network_programming/python_sockets_programming.htm

[2] Docs at https://docs.python.org/3/howto/sockets.html
