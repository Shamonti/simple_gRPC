import grpc
from django.http import JsonResponse
import math_pb2
import math_pb2_grpc

# Create your views here.
def get_add_result(request):
  # Establish a connection with the gRPC server
  channel = grpc.insecure_channel('localhost:50051')
  stub = math_pb2_grpc.MathServiceStub(channel) # Create a stub for the service

  # Extract query parameters (num1 and num2) from the request URL
  num1 = int(request.GET.get('num1', 0))
  num2 = int (request.GET.get('num2', 0))

  add_request = math_pb2.AddRequest(num1=num1, num2=num2)

  response = stub.Add(add_request)

  return JsonResponse({'result': response.result})