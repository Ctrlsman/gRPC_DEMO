from __future__ import print_function

import grpc

from grpc_test.grpc_demo.example import hello_pb2
from grpc_test.grpc_demo.example import hello_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = hello_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(hello_pb2.HelloRequest(name='zds'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()