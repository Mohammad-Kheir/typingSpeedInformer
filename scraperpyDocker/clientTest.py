import socket

HOST = 'localhost'  
PORT = 65004        
EOF = "x23Stop"

USER_ID = "not_not_mk"
NUMBER_OF_SCORES = "1000"

CSoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
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
    

