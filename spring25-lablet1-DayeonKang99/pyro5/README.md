## Setting Up a Virtual Environment in Docker
A virtual Python environment can ensure project isolation, prevents dependency conflicts, and maintains a clean, reproducible, and stable development setup. To create a virtual environment in the docker container, run the below command: 
```
$ python3 -m venv .venv
```
where `.venv` is name of your virtual environment. 

To activate the virtual environment, run 
```
$ source .venv/bin/activate
```
Now, you should see a prefix `(.venv)` preceeding the terminal name. 

**Note:**
Make sure that the virtual environment is created in the *lablet1* directory in the docker container (i.e., cs677-user@4e06f715876f:~/lablet1) rather than the home directory (/home/cs677-user). 
This is because only the lablet1 directory is mounted to the host, and all files in other directories will be deleted when the container is shut down.

Now, you can install the required Pyro5 package for this lablet inside the virtual environment by running:
```
$ pip3 install pyro5
```


## Running the Client and Server Program
First, you need to specify the IP of the server in `greeter-server-simple.py`, `greeter-server.py`and `greeter-client.py`. 
You may first try running both the client and server in the same container. Then, run each in a separate container.

For detailed instructions and explanations of how the program works, see [this guide][]. 

There are two examples: a simple client-server program and one that uses a nameserver. 

### Running the Simple Example
This example consists of two programs, `greeting-server-simple.py` and `greeting-client-simple.py`. These two programs use `pyro5` without
using a name server.
The object name has to be provided as input to the client.

To start the server, first change the IP variable in `greeting-server-simple.py` and run 
```
$ python3 greeting-server-simple.py
```
Then, run the client program using the command below and enter the object uri in the terminal
```
$ python3 greeting-client-simple.py
```

### Running the Nameserver Example
This example uses `greeting-server.py` and `greeting-client.py` use a nameserver and require 
the nameserver to be started (by running `pyro5-ns`) before you start the server.

First, you need to run the nameserver. To do so, run 
```
$ python3 -m Pyro5.nameserver -n <IP> &
```
or
```
$ pyro5-ns -n <IP> &
```

Running the command with `&` at the end will execute the process in the background, allowing you to continue using the same terminal without blocking. 

Then, change the IP variable in greeting-server.py and start the server 
```
$ python3 greeting-server.py
```

Finally, change the IP variable in `greeting-client.py` and run the client
```
$ python3 greeting-client.py
```

[this guide]: https://pyro5.readthedocs.io/en/latest/intro.html


Once you finish this lablet, to deactivate the virtual environment, run
```
$ deactivate
```
