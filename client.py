# ryp-01
import socket
IP = socket.gethostbyname(socket.gethostname())
PORT = 8000
HEADER= 0

client = socket.socket()
client.connect((IP, PORT))
print(f"[CONNECTED] Conectado al servidor en {IP}")
while True:
  msg= input("Ingrese un mensaje:")
  len(msg)
  msg_length = f"´{length}"
  msg_length +="" *(HEADER-len(msg_length))
  client.send(msg_legth.encode("utf-8"))
  client.send(msg.encode("utf-8"))
