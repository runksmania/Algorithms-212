#PQ
from heapq import *

class Graph:
    """A graph node class"""

    #Constructor
    def __init__(self):
        self._graph = {} #Setup hashtable

    def add_vertex(self, node):

        if not node in self._graph:
            self._graph[node] = {} #Internal hash table

    def connect_vertex(self, source, sink, weight, is_bidirectional = False):
        
        if not sink in self._graph:
            self.add_vertex(sink)

        self._graph[source][sink] = weight

        if is_bidirectional == True:
            self.connect_vertex(sink, source, weight)

    def compute_shortest_path(self, start):

        #Tracks known distances
        distances = {}

        #Make sure start is in graph.
        if start in self._graph:

            #Define PQ
            to_visit = []

            #Push starting location
            #By default python will sort PQ by first value in Tuple
            heappush(to_visit, (0, start))

            #While PQ is not empty
            while len(to_visit) > 0:

                #Pop returns item in Python
                top = heappop(to_visit)

                #2nd itm is our key
                key = top[1]

                if not key in distances:

                    #Record distance
                    distances[key] = top[0]

                    #Push children
                    for edge, weight in self._graph[key].items():
                        if not edge in distances:
                            heappush(to_visit, (weight + top[0], edge))

        return distances