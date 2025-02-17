## Quick Start
<!-- 
Note: Some machines have issues running or compiling this code. Linux is the best option and MacOS with the right tools also works. If you have issues, it
is fine to read the code and understand it at a conceptual level.

Install dependencies:

- gcc
- make
- rpcbind
- rpcgen
- libtirpc-dev
--> 

For RPC in C, you will first need to install `libtirpc-dev`, a library that provides support for RPC mechanisms. 

To do so, in the docker container, run 
```
$ sudo apt-get update
$ sudo apt-get install libtirpc-dev
```

Build project:
```
$ make
```

Start `rpcbind` service:

```
$ sudo rpcbind
```

Start the server:

```
$ ./add_server
```

To run the client in the **same container**, open a new terminal and run:
```
$ ./cs677-run-docker
```
Your new terminal will now log in to the same container that hosts the server. 

To start the client, run
```
$ ./add_client <server container IP> 1 2
```

<!-- 

To find the server's container IP address in the host terminal: 
```
$ docker inspect <server container name>
```

or in the server's container terminal: 
```
$ ip a 
```
-->
