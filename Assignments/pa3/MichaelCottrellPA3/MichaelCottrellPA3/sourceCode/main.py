from csv_processor import process_csv
from graph import Graph
from heapq import *

print('***Route Planner***\nNote all input files will assumed to be in the resourceFiles directory.')
map_data = process_csv('resourceFiles/' + input('Enter map file: '))
delivery_data = process_csv('resourceFiles/' + input('Enter delivery file: '))

g = Graph()
deliveries = {}

for i in delivery_data:
  deliveries[i[0]] = 0

start = delivery_data[0][0]
deliveries[start] = 1

for i in map_data:
  g.add_vertex(i[0])
  g.connect_vertex(i[0], i[1], i[2], True)

total_time = 0
path = {}

current = start

while len(path) < len(deliveries) - 1:
  closest = g.shortest_path_dict_nodes(current, deliveries)
  total_time += closest[0]
  path[current] = closest[1][1]
  current = closest[1][0]
  deliveries[current] = 1

print(path)
print(start + ' -> ' + ' -> '.join(path[start].split()))
for i in path:
    if i != start:
        print(i + ' -> ' + ' -> '.join(path[i].split()))