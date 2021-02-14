from concurrent import futures
import time
import grpc
from Protobuffer import messages_pb2, messages_pb2_grpc
from threading import Thread
import random
from setup import URL_GATEWAY

url = URL_GATEWAY


class Equipment:

    def __init__(self, ip, port, name, type_):
        self.ip = ip
        self.port = port
        self.name = name
        self.type = type_

        self.MakeConnection(url)

        self.IdentificateClient()

    def makeStatus(self):
        pass

    def makeUpdate(self, request):
        pass

    def SendStatus(self, time_interval):
        pass

    def GetStatus(self, request, context):
        pass

    def MakeConnection(self, url):
        self.channel = grpc.insecure_channel(url)
        self.stub = messages_pb2_grpc.GatewayServiceStub(self.channel)

    def makeIdentification(self):
        return messages_pb2.Identification(
            name=self.name,
            ip=self.ip,
            port=self.port,
            type=self.type

        )

    def IdentificateClient(self):
        request = self.makeIdentification()

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


