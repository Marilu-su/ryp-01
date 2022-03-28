# ryp-01
import socket
IP = socket.gethostbyname(socket.gethostname())
PORT = 8000
HEADER= 1024
client=socket.socket()
client.connect((IP, PORT))
while True:
  msg= input("Ingrese un mensaje:")
  length = len(msg)
  msg_length = f"´{length}"
  msg_length +="" *(HEADER-len(msg_length))
  client.send(msg_legth.encode("utf-8"))
  client.send(msg.encode("utf-8"))
