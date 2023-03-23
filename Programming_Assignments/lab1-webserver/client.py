from socket import *
clientSocket = socket(AF_INET, SOCK_STREAM)
HOST = "localhost"
PORT = 6789
clientSocket.connect((HOST, PORT))
clientSocket.send("GET /index.html HTTP/1.1\r\n".encode())
clientSocket.send("\r\n".encode())

while True:
    message = clientSocket.recv(1024).decode()

    if not message:
        break

    print(message)
clientSocket.close()
