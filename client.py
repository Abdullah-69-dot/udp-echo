# client.py
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = input("🔹 Enter message to server: ")
client.sendto(msg.encode(), ("127.0.0.1", 12345))

data, _ = client.recvfrom(1024)
print("Server replied:", data.decode())

client.close()