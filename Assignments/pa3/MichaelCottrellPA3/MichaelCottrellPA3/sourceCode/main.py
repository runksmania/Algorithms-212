from csv_processor import process_csv
from graph import Graph
from heapq import *

print('***Route Planner***\nNote all input files will assumed to be in the resourceFiles directory.')
map_file = process_csv('resourceFiles/' + input('Enter map file: '))
delivery_file = process_csv('resourceFiles/' + input('Enter delivery file: '))

g = Graph()

for i in map_file:
    
    #First index is a node.
    g.add_vertex(i[0])

    #Second index is connected node, Third index is weight.
    g.connect_vertex(i[0], i[1], i[2], True)

deliveries = {}
for i in delivery_file:
    deliveries[i[0]] = 0

total_time = 0
path = []

for i in deliveries:
    pq = []
    distances = g.compute_shortest_path(i[0])
    
    for k,v in distances.items():
        if k not in path and k in deliveries:
            heappush(pq, (v[0], v[1]))
        

print("done")