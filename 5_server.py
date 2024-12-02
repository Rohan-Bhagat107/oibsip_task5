import socket
import sys
import time

s=socket.socket()
host=socket.gethostname()
print("Server will start on host: ",host)
port=1010
s.bind((host,port))
print("Server done binding to host and port succesfully")
print()
print("Server is waiting for incomming connection")
s.listen(1)
conn,addr=s.accept()
print(addr,"Has connected to the server and is now online......")
print()
while  1:
    message=input(str("You:>> "))
    message=message.encode()
    conn.send(message)
    print("Message has been sent..")
    incoming_message=conn.recv(1010)
    incoming_message=incoming_message.decode()
    print("Client:>> ",incoming_message)
    print()

    