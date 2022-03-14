import socket

c=socket.socket()
print("Socket Created")
c.connect(('localhost',9999))
print("Socket Connected")
if c.recv(1024)==b'hai varun':
    print("true")
    c.send(bytes('Hi Varun','utf-8'))
else:
    print("false")
