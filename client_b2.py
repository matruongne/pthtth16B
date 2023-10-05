import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 34567

s.connect((host, port))

while True:
    try:
        message = input("Client: ")
        s.send(message.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print(f"Server: {data}")
    except:
        s.close()
        break