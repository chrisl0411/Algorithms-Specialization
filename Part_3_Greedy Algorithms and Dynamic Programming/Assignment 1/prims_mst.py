# Assignment 1
# Problem 3: use Prim's minimum spanning tree algorithm to report the overall cost of a MST

from collections import defaultdict
import heapq

def readFile(dir):
    file = open(dir, 'r')
    header = file.readline().split(' ')
    numNodes = header[0]
    numEdges = header[1]
    currLine = file.readline()
    dict = {}

    #create a dict in a dict, the key is the start node, the values are
    while currLine:
        currEdge = currLine.split(' ')
        node1 = int(currEdge[0])
        node2 = int(currEdge[1])
        edgeCost = int(currEdge[2])
        if node1 in dict:
            dict.get(node1)[node2] = edgeCost
        else:
            dict[node1] = {node2: edgeCost}

        currLine = file.readline()

    return dict

def create_spanning_tree(graph, starting_vertex):
    mst = defaultdict(set)
    visited = set([starting_vertex])
    edges = [
        (cost, starting_vertex, to)
        for to, cost in graph[starting_vertex].items()
    ]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[frm].add(to)
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))

    return mst

if __name__ == "__main__":
    dir = 'C:\\Users\Chris\Documents\Coding\Standford Algorithms Specialization\Part 3 Greedy Algorithms and Dynamic Programming\Assignment 1\edges.txt'

    dict(create_spanning_tree(readFile(dir), 1))