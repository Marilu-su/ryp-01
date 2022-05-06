import socket
from statistics import median_grouped
IP = socket.gethostbyname(socket.gethostname())
PORT = 8000
HEADER= 1024

client = socket.socket()
client.connect((IP, PORT))
print(f"[CONNECTED] Conectado al servidor en {IP}")

while True:
    msg= input("Ingrese un mensaje:")
    msgencd=msg.encode("utf-8")
    medidareal=str(len(msgencd)).encode("utf-8")
    size=len(medidareal)
    cuenta= size*(HEADER-size)
    client.send(cuenta)
    client.send(msgencd)
