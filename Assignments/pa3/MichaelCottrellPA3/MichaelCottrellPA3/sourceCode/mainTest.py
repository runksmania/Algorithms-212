from graph import Graph
from csv_processor import process_csv
g = Graph()

map_data = process_csv('map1.txt')
delivery_data = process_csv('deliveries1.txt')
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

while len(path) < len(deliveries):
  closest = g.shortest_path_dict_nodes(current, deliveries)
  total_time += closest[0]
  path[closest[1][0]] = closest[1][1]
  current = closest[1][0]

print(path)
