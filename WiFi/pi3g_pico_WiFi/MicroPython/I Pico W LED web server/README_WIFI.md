I Pico W LED web server
=======================
Building a Web Based Front End For Our Project
The flipside of being able to send GET requests is that we are also able to respond to them. Other devices on our network can send these requests to our Pi Pico’s network IP address and if it is listening out for these messages we can decode them and take the appropriate action.

The first partners process is to create a network socket that allows the Pico to receive HTTP GET requests and capture the data ready for us to process. To do this we need to use the socket library.

import socket
# Open socket
# addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
addr = (pico_ip, 80)
s = socket.socket()
s.bind(addr)
s.listen(1)
print('listening on', addr)
A socket is basically a data stream object that connects our code to a port on the network. This port is basically a doorway that we open to allow data in and out. Different port numbers are used for different network services. Port 80 is the default port for HTTP traffic.

So we first need to create an address tuple that contains our Pico’s network IP address and port number we want to use. We then create a socket object and bind it to this address combination. Once a socket is bound to a port we can tell it to start listening for other devices connecting to it.
