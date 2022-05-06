import socket as s

IP = s.gethostbyname(s.gethostname())
PORT = 8000
HEADER = 1024

server= s.socket()
server.bind((IP,PORT))
server.listen()
print(f"[LISTENGING] El servidor esta esperando conexiones en {IP}")

conn, add = server.accept()
connected= True
print (f"nueva coneccion{add}")

while connected:
    encoded=conn.recv(HEADER)
    msg=encoded.decode("utf-8")
    mensaje=conn.recv(msg).decode("utf-8")
    print(f"[CLIENT]Recibi:{mensaje}")
    if mensaje == "close" :
            break
