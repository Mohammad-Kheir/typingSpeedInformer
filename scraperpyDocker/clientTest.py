import socket
import sys


HOST = 'localhost'  
PORT = int(sys.argv[1])        
EOF = "x23Stop"

USER_ID = "not_not_mk"
NUMBER_OF_SCORES = "1000"

CSoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
CSoc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
CSoc.connect((HOST, PORT))
CSoc.sendall(f"{USER_ID} {NUMBER_OF_SCORES}".encode())
app = bytearray(b'')
x = 1

while True:
    data = CSoc.recv(8000)
    print(x)
    if data == EOF.encode():
        break
    app += data
    x += 1

print(app.decode("utf-8"))
    

