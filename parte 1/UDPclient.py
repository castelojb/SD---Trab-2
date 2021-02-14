import sys
import socket
from operations import make_json, json_to_bytes, bytes_to_json
from setup import *

# get server location
serverAddressPort = (SERVERIP, SERVERPORT)

# get bufferSize
bufferSize = 1024

# make UDP socket
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

if __name__ == '__main__':

    # check if 3 args ara passed
    if len(sys.argv[1:]) == 3:

        # get args
        val1 = sys.argv[1]
        op = sys.argv[2]
        val2 = sys.argv[3]

        # make json to send for server
        msgFromClient = make_json(val1, val2, op)

        # transform the json in bytes
        bytesToSend = json_to_bytes(msgFromClient)

        # send message for server
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)

        # receive message from server
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)[0]

        # show final response
        result = bytes_to_json(msgFromServer)['response']
        out = f'{val1} {op} {val2} = {result}'
        print(out)
