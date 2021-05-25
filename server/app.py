from flask import Flask
from flask import request
from flask_cors import CORS
import move_service

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/calculate", methods=['POST'])
def calculate():
  move = move_service.getBestMove(request.json['board'], request.json['player'])
  return str(move)