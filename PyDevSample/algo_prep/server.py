import socket
s=socket.socket()
print("Socket Created")
s.bind(('localhost',9999))
print("Socket Binded")
s.listen(1)
print("Waiting for connections")
while True:
    clientsocket,addr=s.accept() #sending the data through the client socket
    print("connected with ",addr)
    clientsocket.send(bytes('hai varun','utf-8'))
    print(clientsocket.recv(1024))
    clientsocket.close()
    