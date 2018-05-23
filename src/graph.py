from networkx import Graph, shortest_path, from_numpy_matrix
import numpy
matrix = [[('0-1', 2), ('0-2', 1), ('0-3', 1)],
          [('1-1', 0), ('1-2', 0), ('1-3', 1)],
          [('2-1', 0), ('2-2', 2), ('2-3', 1)]]

# start & end
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
print(path)
