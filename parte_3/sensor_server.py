from models import Sensor
import grpc
from concurrent import futures
from Protobuffer import messages_pb2_grpc
import time

ip = '0.0.0.0'

port = 8000

external_ip = '0.0.0.0'

term = Sensor(external_ip, port, 'TERMOMETRO DE TERESINA')


if __name__ == '__main__':

    # Run a gRPC server with one thread.
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))

    # Adds the servicer class to the server.
    messages_pb2_grpc.add_EquipmentServiceServicer_to_server(term, server)

    server.add_insecure_port(f'{ip}:{port}')

    server.start()

    print(f'API server started. Listening at {ip}:{port}.')

    while True:
        time.sleep(60)
