# coding:utf-8

import grpc
import data_pb2 as pb2
import data_pb2_grpc as pb2_grpc
import time
import random

_HOST = 'localhost'
_PORT = '8005'


def test():
    while 1:
        time.sleep(1)
        data = str(random.random())
        yield pb2.TestClientSendStreamRequest(data=data)


def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = pb2_grpc.TestClientSendStub(channel=conn)

    response = client.TestClientSendStream(test())
    print(response.result)


if __name__ == '__main__':
    run()
