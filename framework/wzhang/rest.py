from flask import Flask, jsonify
import grpc
import requests
from wzhang.grpc_server import calculator_pb2, calculator_pb2_grpc

# import the generated classes

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# Rest API Call
@app.route('/api/posts/<id>')
def posts(id):
    post_url = "https://jsonplaceholder.typicode.com/todos/" + id
    r = requests.get(post_url)
    return r.json()

# gRPC API Call
@app.route('/api/calculator/<num>')
def calculator(num):
    # open a gRPC channel
    channel = grpc.insecure_channel('localhost:50051')

    # create a stub (client)
    number = calculator_pb2.Number(value=int(num))
    response = calculator_pb2_grpc.CalculatorStub(channel).SquareRoot(number)
    return jsonify(response.value)
