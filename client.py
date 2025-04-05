import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')  
    stub = calculator_pb2_grpc.CalculatorStub(channel)
    request = calculator_pb2.SumRequest(a=7, b=5)
    response = stub.Sum(request)
    print(f"O resultado da soma é: {response.result}")

if __name__ == '__main__':
    run()