import argparse
import time
from socket import *

ap = argparse.ArgumentParser()
ap.add_argument(
    "-H", "--host", default="192.168.5.6",
    help="UDP Host")
ap.add_argument(
    "-P", "--port", type=int, default=6000,
    help="Port for remote UDP host")
ap.add_argument(
    "-m", "--msgsize", type=int, default=2,
    help="message size for UDP test")
ap.add_argument(
    "-M", "--msgtotal", type=int, default=1000,
    help="total message for UDP test")
ap.add_argument(
    "-d", "--delay", type=float, default=10,
    help="delay between message")
args = vars(ap.parse_args())

host        = args["host"]
port        = args["port"]
msgSize     = args["msgsize"]
msgTotal    = args["msgtotal"]
delay       = args["delay"]

for i in range(msgTotal):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    # clientSocket.settimeout(1)
    message = 'x'*msgSize
    addr = (host, port)

    start = time.time()
    clientSocket.sendto(message, addr)
    try:
        data, server = clientSocket.recvfrom(1024)
        end = time.time()
        elapsed = end - start
        print 'latency %d' % (elapsed)
    except timeout:
        print 'REQUEST TIMED OUT'
    time.sleep(1.0/delay)
