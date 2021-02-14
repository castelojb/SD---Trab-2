from models import Actuator
import grpc
from concurrent import futures
from Protobuffer import messages_pb2_grpc
import time

ip = '0.0.0.0'

port = 8080

external_ip = '0.0.0.0'

refri = Actuator(external_ip, port, 'REFRIGERADOR DO INFERNO')


if __name__ == '__main__':

    # Run a gRPC server with one thread.
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))

    # Adds the servicer class to the server.
    messages_pb2_grpc.add_EquipmentServiceServicer_to_server(refri, server)

    server.add_insecure_port(f'{ip}:{port}')

    server.start()

    print(f'API server started. Listening at {ip}:{port}.')

    while True:
        time.sleep(60)