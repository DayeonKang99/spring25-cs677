In this part, we will following the Getting Started with Java RMI tutorial

https://docs.oracle.com/javase/8/docs/technotes/guides/rmi/hello/hello-world.html

**Note:** Make sure you use the absolute path `/home/cs677-user/lablet1/rmi` as the `destDir` and `classDir` when following the guide. 

To run the client program and the server program in two separate containers, set the server's container IP address accordingly in Line 51 of `Client.java`. 
```
Line 51: Registry registry = LocateRegistry.getRegistry("CONTAINERS_IP");
```

To start a new container, open a new terminal and run the script with the `-f` flag as shown below:
```
$ ./cs677-run-docker -f
```


<!-- 

To find the server's container IP address, in the host terminal, run 
```
$ docker inspect <server container name>
```

or in the container's terminal, run
```
$ ip a
```

```
javac -d /home/cs677-user/lablet1/rmi Hello.java Server.java Client.java
```

```
rmiregistry &
```

Start the server:
```
java -classpath /home/cs677-user/lablet1/rmi -Djava.rmi.server.codebase=file:/home/cs677-user/lablet1/rmi/ example.hello.Server &
```

From another terminal, start the client:
```
java  -classpath /home/cs677-user/lablet1/rmi example.hello.Client
```
-->
