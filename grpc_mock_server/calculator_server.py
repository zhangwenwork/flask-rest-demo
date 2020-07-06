import grpc
from concurrent import futures
import time

# import the generated classes
import calculator_pb2_grpc, calculator_pb2


# create a class to define the server functions
# derived from calculator_pb2_grpc.CalculatorServicer
class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):

    # calculator.square_root is exposed here
    # the request and response are of the data types
    # generated as calculator_pb2.Number
    def SquareRoot(self, request, context):
        print('mock call...........')
        response = calculator_pb2.Number()
        # Mock Value equals 6.0
        response.value = 6.0
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the created server
calculator_pb2_grpc.add_CalculatorServicer_to_server(
        CalculatorServicer(), server)

# listen on port 50051
print('Starting mock server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)