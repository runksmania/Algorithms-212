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

            #Define PQ.
            to_visit = []

            #Push starting location.
            #Our tuple has a second tuple which stores the edge and its current path from start.
            #Which in this case is empty.
            heappush(to_visit, (0, (start, "")))

            #While PQ is not empty.
            while len(to_visit) > 0:

                #Pop top vertex.
                top = heappop(to_visit)

                #First item of the inner tuple is our edge name key. 
                key = top[1][0]

                if not key in distances:

                    #Push a tuple containing:
                    #    1. The distance to get here.
                    #    2. The path taken to get here.
                    distances[key] = (top[0], top[1][1])

                    #Push children onto heap if not seen before.
                    for edge, weight in self._graph[key].items():
                        if not edge in distances:
                            
                            #Push into the heap a tuple containing:
                            #    1. The weight of this edge + previous path's weight.
                            #    2. A tuple containing:
                            #        I. The edge name to be our lookup key.
                            #        II. The path to this edge + this edge name.
                            heappush(to_visit, (float(weight) + top[0], (edge, top[1][1] + " " + edge)))

        return distances
