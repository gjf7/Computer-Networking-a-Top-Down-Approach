# import socket module
from socket import *
import sys  # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)  # Prepare a sever socket
HOST = ''
PORT = 6789
serverSocket.bind((HOST, PORT))
serverSocket.listen(1)
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, connectionAddress = serverSocket.accept()
    print('Accpeted from ', connectionAddress)
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
        connectionSocket.send("Sent-By: Hao Chen \r\n".encode())
        connectionSocket.send("\r\n".encode())
        # Send the content of the requested file to the client
        connectionSocket.send(outputdata.encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 NOT FOUND\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
