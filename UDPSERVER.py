import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(("127.0.0.1", 12345))
print("UDP Server is waiting for one message...")

data, client_address = server_socket.recvfrom(1024)  
print(f"Received from {client_address}: {data.decode()}")

server_socket.sendto(b"Message received. Goodbye!", client_address)
print("Reply sent. Server will now close.")

server_socket.close()
