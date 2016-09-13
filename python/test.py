import time
from socket import *

host = "192.168.5.6"
port = 6000
# clientSocket = socket(AF_INET, SOCK_DGRAM)
# serverSocket = socket(AF_INET, SOCK_DGRAM)
# serverSocket.bind(('', 5000))
for pings in range(10):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1)
    # clientSocket.bind("192.168.5.1", 5000)
    message = 'test'
    addr = (host, port)

    start = time.time()
    clientSocket.sendto(message, addr)
    try:
        data, server = clientSocket.recvfrom(1024)
        end = time.time()
        elapsed = end - start
        print '%s %d %d' % (data, pings, elapsed)
    except timeout:
        print 'REQUEST TIMED OUT'
