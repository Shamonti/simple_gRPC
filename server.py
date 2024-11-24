import grpc
from concurrent import futures
import time

import math_pb2_grpc
import math_pb2

# Implement the MathService
class MathServiceServicer(math_pb2_grpc.MathServiceServicer):
  def Add(self, request, context):
    # Perform the addition operation
    result = request.num1 + request.num2

    # Return the response with result
    return math_pb2.AddResponse(result=result)
  
  # Start the gRPC server
def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  math_pb2_grpc.add_MathServiceServicer_to_server(MathServiceServicer(), server)
  server.add_insecure_port('[::]:50051') # Port on which the server will listen
  server.start()
  print("gRPC server is running on port 50051...")

  try:
    while True:
      time.sleep(60 * 60 * 24) # Keep the server alive

  except KeyboardInterrupt:
    server.stop(0)

if __name__== '__main__':
  serve()