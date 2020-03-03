#! /usr/bin/env python3
import fileinput
import sys

class Edge:
    def __init__(self, instr, label):
        self.label = label
        info = instr.split()
        self.vertices = (int(info[0]), int(info[1]))
        self.weight = float(info[2])

    def getVertices(self):
        return self.vertices

    def getWeight(self):
        return self.weight

    def __repr__(self):
        str = "{:>4d}: ".format(self.label)
        str += "({0}, {1}) {2}".format(self.vertices[0], self.vertices[1], self.weight)
        return str

    def __str__(self):
        str = "{:>4d}: ".format(self.label)
        str += "({0}, {1}) {2}".format(self.vertices[0], self.vertices[1], self.weight)
        return str

def getGraph():
    if len(sys.argv) != 3:
        print("Usage: MWST input_file output_file")
        sys.exit(1)
    in_file = sys.argv[1]
    ifd = open(in_file, 'r')
    content = ifd.read().split('\n')
    ifd.close()
    # mock data
    # content = "7\n11\n1 2 6\n1 4 3\n2 3 5\n2 5 8\n3 5 1\n3 7 4\n4 5 7\n4 6 9\n5 6 6\n5 7 5\n6 7 2"
    # content = content.split('\n')
    numV = int(content[0])
    numE = int(content[1])
    content = content[2:-1]
    graph = [Edge(content[i], i+1) for i in range(len(content)) if len(content[i]) >= 5]
    return graph, numV

def sortGraph(graph):
    graph.sort(key = lambda c: c.getWeight())
    return graph

def findMinTree(graph, numV):
    tree = list()
    totalWeight = 0.0
    i = 0
    connected = list()
    while len(tree) < numV-1 and i < len(graph):
        v1, v2 = graph[i].getVertices()
        if not isPathExist(connected, v1, v2) and not isPathExist(connected, v2, v1):
            tree.append(graph[i])
            totalWeight += graph[i].getWeight()
            connected = update(connected, v1, v2)
        i += 1
    return tree, totalWeight    

def isPathExist(connected, v1, v2):
    for i in connected:
        if v1 in i and v2 in i:
            return True
    return False

def update(connected, v1, v2):
    if len(connected) == 0:
        connected.append([v1, v2])
        return connected
    for i in range(len(connected)):
        if v1 in connected[i]:
            connected[i].append(v2)
        elif v2 in connected[i]:
            connected[i].append(v1)
        else:
            connected.append([v1, v2])
    return connected
        
def main():
    graph, numV = getGraph()
    graph = sortGraph(graph)
    tree, total = findMinTree(graph, numV)
    out_file = sys.argv[2]
    ofd = open(out_file, "w")
    for i in tree:
        ofd.write(str(i))
        ofd.write('\n')
    ofd.write("Total Weight = %.2f\n" %(total))
    ofd.close()

if __name__ == "__main__":
    main()