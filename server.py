import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345

s.bind((host, port))
s.listen(5)

client_socket, client_address = s.accept()
print(f"Đã kết nối từ {client_address}")
while True:
    data = client_socket.recv(1024).decode('utf-8')
    if not data:
        break
    print(f"Client: {data}")
    client_socket.send(data.encode('utf-8'))
client_socket.close()
