## Setting Up a Virtual Environment in Docker
A virtual Python environment can ensure project isolation, prevents dependency conflicts, and maintains a clean, reproducible, and stable development setup. 
First, start the docker container
```
$ ./cs677-run-docker
```
To create a virtual environment, in the docker container, run the below command: 
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
$ pip3 install grpcio grpcio-tools
$ pip3 install protobuf==3.20.*
```

## Running the Client and Server Program
Before running the programs, you first need to update the IP and port of the server in `greeter_server.py` and `greeter_client.py`

Then, inside the container, run the server by executing 

```
$ python3 greeter_server.py
```

After that, we can test the client program in a separate container. Open a new terminal and run the below command to start a new container. 
```
$ ./cs677-run-docker -f
```

In the new container, run the below command to start the client. 
```
$ python3 greeter_client.py
```

Once you finish this lablet, to deactivate the virtual environment, run
```
$ deactivate
```
