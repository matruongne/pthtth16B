import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 34567

s.bind((host, port))
s.listen(5)

client, client_addr = s.accept()
print(f"Đã kết nối từ {client_addr}")
while True:
    data = client.recv(1024).decode('utf-8')
    if not data:
        break
    print(f"Client: {data}")
    client.send(data.upper().encode('utf-8'))
client.close()
