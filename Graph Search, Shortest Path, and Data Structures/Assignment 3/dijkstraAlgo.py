import sys

def parseGraph(dir):
    # each vertex represented in dictionary data type with format: {vertex_1: [(vertex_2,weight),(vertex_3,weight),...],...}
    vertices = {}
    for line in open(dir, 'r'):
        fields = [f for f in line.split()]
        vertex = int(fields.pop(0))

        # for each pair in the line, creates a tuple splitting using comma as delimiter example: (80, 982)
        edges = [tuple([int(t) for t in f.split(',')]) for f in fields]
        vertices[vertex] = edges

    return vertices

def dijkstras(vertices, targets):
    X = {1: True}
    A = {1: 0}

    while len(X) != len(vertices):
        min_src = 0
        min_dst = 0
        min_weight = sys.maxsize #maxsize is place holder to make sure initial comparison of A[u] + l_uv is always less
        for u in X:
            for v, l_uv in vertices[u]:
                if v in X:
                    continue
                if A[u] + l_uv < min_weight:
                    min_src, min_dst = u, v
                    min_weight = A[u] + l_uv
        if min_src == 0:
            print ('Found nothing to match the greedy criterion! X = %s' % X)
            sys.exit(1)
        X[min_dst] = True
        A[min_dst] = min_weight
    print ([A[t] for t in targets])



# class Graph():
#     def __init__(self, vertices):
#         self.vertices = vertices
#         self.edges = defaultdict(list)
#         self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
#
#     def get_graph(self):
#         return self.graph
#
#     def minDistance(self, dist, sptSet):
#         min = sys.maxsize;
#
#         for v in range(self.V):
#             if dist[v] < min and sptSet[v] == False:
#                 min = dist[v]
#                 min_index = v
#         return min_index
#
#     def dijkstra(self,src):
#         dist = [sys.maxsize] * self.V
#         dist[src] = 0
#         sptSet = [False] * self.V
#
#         for cout in range(self.V):
#             u = self.minDistance(dist, sptSet)
#             sptSet[u] = True
#             for v in range(self.V):
#                 if self.graph[u][v] > 0 and sptSet[V] and dist[v] > dist[u]+self.graph[u][v]:
#                     dist[v] = dist[u] + self.graph[u][v]
#
#         return Graph.get_graph()

if __name__ == "__main__":
    dir = "C:\\Users\Chris\Documents\Coding\Standford Algorithms Specialization\Part 2_Graphs\Assignment2_dijkstraData.txt"
    target = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]

    dijkstras(parseGraph(dir), target)

