import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print 'Recieved connection from: ', addr
    c.send('Welcome home')
    c.close()
