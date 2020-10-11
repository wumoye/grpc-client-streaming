# coding:utf-8

import time

import grpc
import data_pb2 as pb2
import data_pb2_grpc as pb2_grpc

from concurrent import futures

_HOST = 'localhost'
_PORT = '8005'


class TestClientSend(pb2_grpc.TestClientSendServicer):
    def TestClientSendStream(self, request_iterator, context):
        for request in request_iterator:
            print(request.data)
        return pb2.TestClientSendStreamResponse(result='ok')


def run():
    grpc_server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=4)
    )
    pb2_grpc.add_TestClientSendServicer_to_server(TestClientSend(), grpc_server)
    grpc_server.add_insecure_port(_HOST + ':' + _PORT)
    print(f'server will start at {_HOST}:{_PORT}')
    grpc_server.start()

    try:
        while 1:
            time.sleep(3600)
    except KeyboardInterrupt:
        grpc_server.stop(0)


if __name__ == '__main__':
    run()
