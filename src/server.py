from flask import Flask
from networkx import shortest_path, Graph
from flask_restful import Resource, Api
from graphapi import GraphAPI
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(GraphAPI, '/graph')
