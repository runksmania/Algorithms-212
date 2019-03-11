import sys
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

for i in map_data:
  g.add_vertex(i[0])
  g.connect_vertex(i[0], i[1], i[2], True)

total_time = sys.maxsize
path = {}
start = ''

for i in delivery_data:
  current_start = i[0]
  delivery_current = deliveries.copy()
  delivery_current[current_start] = 1
  current = current_start
  delivery_time = 0
  current_path = {}

  while len(current_path) < len(delivery_current) - 1:
    closest = g.shortest_path_dict_nodes(current, delivery_current)
    
    if closest != 0:
      delivery_time += closest[0]
      current_path[current] = closest[1][1]
      current = closest[1][0]
      delivery_current[current] = 1
    else:
      break
  
  if delivery_time < total_time:
    total_time = delivery_time
    path = current_path
    start = current_start
  

print(path)
print(total_time)
print(start + ' -> ' + ' -> '.join(path[start].split()))
for i in path:
    if i != start:
        print(i + ' -> ' + ' -> '.join(path[i].split()))
