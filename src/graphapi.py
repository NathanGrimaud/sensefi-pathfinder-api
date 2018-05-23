from networkx import Graph, shortest_path
from flask_restful import Resource, reqparse
from flask import request
from typing import Type


def to_tuple(edge):
    return (edge[0], edge[1])


class Node():

    top = None
    bottom = None
    left = None
    right = None

    def from_list(list)->'Node':
        # lol
        "lol"

    def __init__(self, top: 'Node', bottom: 'Node', left: 'Node', right: 'Node'):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right


class GraphAPI(Resource):
    """
    we will receive a set of data:

    """

    def post(self):
        content = request.get_json()
        matrix = content.get('nodes')
        print(matrix)
        points = []
        for y, line in enumerate(matrix):
            for x, item in enumerate(line):
                if (item[1] is 2):
                    points.append(item)
                    matrix[y][x] = (item[0], 1)

        def to_name(tlp):
            return tlp[0]

        def extract_line(line):
            return list(map(to_name, line))

        names = list(map(extract_line, matrix))

        G = Graph()
        for line in names:
            G.add_nodes_from(line)

        for y, line in enumerate(matrix):
            for x, item in enumerate(line):
                if (x+1 < len(line)):
                    if ((item[1] is 1) and (line[x+1][1] is 1)):
                        G.add_edge(item[0], line[x+1][0])
                if (y+1 < len(matrix)):
                    if ((item[1] is 1) and (matrix[y+1][x][1] is 1)):
                        G.add_edge(item[0], matrix[y+1][x][0])

        path = shortest_path(G, source=points.pop()[0], target=points.pop()[0])
        return path
