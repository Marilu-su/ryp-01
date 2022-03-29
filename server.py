import socket as s
IP = s.gethostbyname(s.gethostname())
PORT = 8000
HEADER = 0
server= s.socket()
server.bind((IP,PORT))
server.listen()
print(f"[LISTENGING] El servidor esta esperando conexiones en {IP}")

While True:
    conn, add = server.accept()
    connected= True
    print (f"nueva coneccion{addr}")
    while connected:
        msg = conn.recv()
        print(f"{msg.decode(´utf-8´)}")
        print(f"Recibido")
        if (msg=="close")
        connected= False
    
    
