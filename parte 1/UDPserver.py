import socket
from operations import parse_json, json_to_bytes, bytes_to_json
from setup import *

# get server location
localIP = SERVERIP
localPort = SERVERPORT

# get buffer size
bufferSize = 1024

# make UDP socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

if __name__ == '__main__':

    # initializing server
    UDPServerSocket.bind((localIP, localPort))

    print("UDP server up and listening")

    while True:
        # receiving message from the port
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

        # get content
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]

        # get json from client
        json_ = bytes_to_json(message)

        # make operation
        msgFromServer = parse_json(json_)

        # turning json into bytes
        bytesToSend = json_to_bytes(msgFromServer)

        # sending message to the customer
        UDPServerSocket.sendto(bytesToSend, address)
