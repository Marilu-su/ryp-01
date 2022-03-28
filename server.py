import socket as s
IP = s.gethostbyname(s.gethostname())
PORT = 8000
HEADER = 1024
server= s.socket()
server.bind((IP,PORT))
server.listen()

While True:
    conn, add = server.accept()
    connected= True
    print (f"nueva coneccion{addr}")
    while connected:
        length = conn.recv(HEADER)
        length = int(length.decode("utf-8"))
        msg = conn.recv(legth)
        print(f"{msg.decode(´utf-8´)}")
    
    
