from concurrent import futures
import time
import grpc
from Protobuffer import messages_pb2, messages_pb2_grpc
from threading import Thread
import random
from setup import URL_GATEWAY, MULTICAST_GROUP, SERVER_ADRESS
import socket
import struct



class Equipment:

    def __init__(self, ip, port, name, type_):
        self.ip = ip
        self.port = port
        self.name = name
        self.type = type_

        self.MakeConnection(URL_GATEWAY)

        self.IdentificateClient()

    def makeStatus(self):
        pass

    def makeUpdate(self, request):
        pass

    def SendStatus(self, time_interval):
        pass

    def GetStatus(self, request, context):
        pass

    def MakeGRPCConnection(self, url):
        self.channel = grpc.insecure_channel(url)
        self.stub = messages_pb2_grpc.GatewayServiceStub(self.channel)

    def MakeMulticast(self):
        print('init multicast')
        udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # on this port, receives ALL multicast groups
        udp_sock.bind(SERVER_ADRESS)

        mreq = struct.pack('4sl', socket.inet_aton(MULTICAST_GROUP), socket.INADDR_ANY)

        udp_sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

        data, address = udp_sock.recv(10240)
        print(data)

        self.MakeGRPCConnection(URL_GATEWAY)

    def MakeConnection(self, url):
        self.MakeGRPCConnection(url)


    def makeIdentification(self):
        return messages_pb2.Identification(
            name=self.name,
            ip=self.ip,
            port=self.port,
            type=self.type

        )

    def IdentificateClient(self):
        request = self.makeIdentification()

        try:
            response = self.stub.Identificate(request)

        except Exception as e:
            self.MakeMulticast()
            response = self.stub.Identificate(request)


        self._id = response.value

    def Identificate(self, request, context):
        out = messages_pb2.Identification(
            name=self.name,
            ip=self.ip,
            port=self.port

        )

        return out

    def ReceiveUpdate(self, request, context):

        self.makeUpdate(request)

        return messages_pb2.google_dot_protobuf_dot_empty__pb2.Empty()


class Sensor(Equipment):

    def __init__(self, ip, port, name):
        super().__init__(ip, port, name, messages_pb2.SENSOR)

        self.temp = random.randint(0, 100)

        thread = Thread(target=self.SendStatus, args=[10])

        thread.start()

    def makeStatus(self):
        return messages_pb2.Status(
            payload=self.temp,
            type=messages_pb2.TEMPERATURE,
            id=self._id
        )

    def SendStatus(self, args):
        while True:
            stats = self.makeStatus()

            response = self.stub.ReceiveStatus(stats)
            self.temp = random.randint(0, 100)

            time.sleep(args)

            print(response)


class Actuator(Equipment):

    def __init__(self, ip, port, name):

        super().__init__(ip, port, name, messages_pb2.ACTUATOR)

        self.temp = random.randint(0, 100)

        self.power = True
        
        self.SendStatus(messages_pb2.TURN_ON_OFF)
        
        self.SendStatus(messages_pb2.TEMPERATURE)


    def SendStatus(self, type_):

        stats = self.makeStatus({'type': type_})

        response = self.stub.ReceiveStatus(stats)

        print(response)

    def makeUpdate(self, request):

        if request.type == messages_pb2.TURN_ON_OFF:
            self.power = request.payload

        if request.type == messages_pb2.TEMPERATURE:
            self.temp = request.payload

    def makeStatus(self, type_):

        if type_ == messages_pb2.TURN_ON_OFF:
            return messages_pb2.Status(
                payload=self.power,
                type=type_,
                id=self._id
            )

        if type_ == messages_pb2.TEMPERATURE:
            return messages_pb2.Status(
                payload=self.temp,
                type=type_,
                id=self._id
            )

    def GetStatus(self, request, context):

        response = self.makeStatus(request.type)

        return response


