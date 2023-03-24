from socket import *
from time import time
from math import floor

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

HOST = "localhost"
PORT = 12000
PROBE_MESSAGE = "HELLO"
clientSocket.connect((HOST, PORT))

for i in range(10):
    startMs = time() * 1000
    clientSocket.send(PROBE_MESSAGE.encode())

    timeText = ""
    try:
        message = clientSocket.recv(1024).decode()
        endMs = time() * 1000
        timeText = str(floor(endMs - startMs)) + "ms"
    except timeout:
        timeText = "timeout"
    message = "Ping " + str(i) + " TTL=" + timeText
    print(message)
