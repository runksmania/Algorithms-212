#
#Assignment: PA3
#Description: Perform and analyze min span trees with Dijkstra's shortest path algorithm.
#Author: Michael Cottrell
#HSU ID: 946839472
#Completion Time: 5 hours.
#In completing this program, I received help from the following people:
#N/A
#

#PQ
from heapq import *

class Graph:
    """A graph node class"""

    #Constructor
    def __init__(self):
        self._graph = {} #Setup hashtable

    #Inserts the vertex into the graph hashtable and assigns a hashtable to it.
    #Time Complexity: O(1)
    #Space Complexity: O(1)
    def add_vertex(self, node):

        if not node in self._graph:
            self._graph[node] = {} #Internal hash table

    #Connects the verticies together and adds the sink vertex to the graph if it doesn't exist.
    #Time Complexity: O(1)
    #Space Complexity: O(1)
    def connect_vertex(self, source, sink, weight, is_bidirectional=False):
        
        if not sink in self._graph:
            self.add_vertex(sink)

        self._graph[source][sink] = weight

        if is_bidirectional == True:
            self.connect_vertex(sink, source, weight)

    #Function to compute the shortest paths between a vertex given and all connecting paths.
    #Returns a hash table containing tuple values. Each tuple has a time in seconds and a path string.
    #Time Complexity: O(E*Log(E))
    #Space Complexity: O(V) 
    #E = number of edges.
    #V = number of vertices.
    def compute_shortest_path(self, start):

        #Tracks known distances
        distances = {}

        #Make sure start is in graph.
        if start in self._graph:

            #Define PQ.
            to_visit = []

            #Push starting location.
            #Our tuple has a second tuple which stores the edge and its current
            #path from start.
            #Which in this case is empty.
            heappush(to_visit, (0, (start, "")))

            #While PQ is not empty.
            while len(to_visit) > 0:

                #Pop top vertex.
                top = heappop(to_visit)

                #First item of the inner tuple is our edge name key.
                key = top[1][0]

                if not key in distances:

                    #Insert a tuple containing:
                    #    1.  The distance to get here.
                    #    2.  The path taken to get here.
                    distances[key] = (top[0], top[1][1])

                    #Push children onto heap if not seen before.
                    for edge, weight in self._graph[key].items():
                        if not edge in distances:
                            
                            #Push into the heap a tuple containing:
                            #    1.  The weight of this edge + previous path's
                            #    weight.
                            #    2.  A tuple containing:
                            #        I.  The edge name to be our lookup key.
                            #        II.  The path to this edge + this edge
                            #        name.
                            heappush(to_visit, (float(weight) + top[0], (edge, top[1][1] + " " + edge)))

        return distances

    #This function finds the shortest path based off of dijkstra's aglorithm.
    #It also uses a dictionary of nodes to visit.  
    #It returns a tuple containing the path to the closest node in dict_nodes
    #Time Complexity: O(E*Log(E))
    #Space Complexity: O(V)
    def shortest_path_dict_nodes(self, start, dict_nodes):
      
      if start in self._graph:
        
        #Define PQ
        to_visit = []

        #Tracks previously seen nodes.
        seen = {}

        #Push starting location.
        #Our tuple has a second tuple which stores the edge and its current
        #path from start.
        #Which in this case is empty.
        heappush(to_visit, (0, (start, "")))

        while len(to_visit) > 0:

          #Pop top add_vertx.
          top = heappop(to_visit)

          #First item of the inner tuple is our edge name key.
          key = top[1][0]

          if key in dict_nodes and dict_nodes[key] == 0:
            return top

          if key not in seen:

            seen[key] = 0

            #Push children onto heap if not seen before.
            for edge, weight in self._graph[key].items():

              if edge not in seen:

                #Push into the heap a tuple containing:
                #    1.  The weight of this edge + previous path's
                #    weight.
                #    2.  A tuple containing:
                #        I.  The edge name to be our lookup key.
                #        II.  The path to this edge + this edge
                #        name.
                heappush(to_visit, (int(weight) + top[0], (edge, top[1][1] + " " + edge)))
      
      return 0
