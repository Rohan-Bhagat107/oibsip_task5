import socket
import sys
import time

s=socket.socket()
host=input(str("Please enter the host name of the server: "))
port=1010
s.connect((host,port))
print("Connected to chat succefully")
while 1:
    incoming_message=s.recv(1010)
    incoming_message=incoming_message.decode()
    print("Server:>> ",incoming_message)
    print()
    message=input(str("You:>> "))
    message=message.encode()
    s.send(message)
