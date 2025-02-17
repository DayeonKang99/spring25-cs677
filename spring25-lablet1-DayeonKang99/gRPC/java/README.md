[This code's documentation lives on the grpc.io site.](https://grpc.io/docs/languages/java/quickstart)

## Quick Start

Before running the server and the client, you will need to update the IP and port of the server in two programs. 
Modify Line 65 in gRPC/java/src/main/java/io/grpc/examples/helloworld/HelloWorldClient.java
```
Line 65 String target = "193.0.0.1:5555";
```
where 193.0.0.1 is the sever's container IP and 5555 is the server's container exposed port. 

Modify Line 36 in gRPC/java/src/main/java/io/grpc/examples/helloworld/HelloWorldServer.java
```
Line 36: int port = 5555;
```

You can now build the project. To do so, first start a docker container and run:

```
$ ./gradlew installDist
```

Then run the server:
```
$ ./build/install/java/bin/hello-world-server
```

To run the client in another container, open a new terminal and run 
```
$ ./cs677-run-docker -f
```
to start a new container. 

In the newly created container, run the below command to start the client
```
$ ./build/install/java/bin/hello-world-client
```
