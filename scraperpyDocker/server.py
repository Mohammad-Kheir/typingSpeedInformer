import socket as s
from time import sleep
from typeracerScraper_package import typeracerScraper as t

HOST = "localhost"
PORT = 65004
EOF = "x23Stop"


mySoc = s.socket(s.AF_INET, s.SOCK_STREAM)
mySoc.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
mySoc.bind((HOST, PORT))
mySoc.listen()
conn, addr = mySoc.accept()

print(f"{conn} {addr}")

while True:
    data = conn.recv(8000)

    if not data:
        break
    

    para = data.decode().split()
    df = t.TypeRacerScraper(para[0], para[1]).result_json()
    input = df

    splitLen = 1024  
    for lines in range(0, len(input), splitLen): 
            outputData = input[lines:lines+splitLen] 
            conn.send(outputData.encode()) 
            sleep(0.05)
     
    conn.send(EOF.encode())


conn.close()
