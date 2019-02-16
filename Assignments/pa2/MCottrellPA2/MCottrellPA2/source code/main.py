from csv_processor import process_csv
from graph import Graph
from node_building_connector import NodeBuildingConnector

distances = process_csv("./resource files/distances.csv")
graph = Graph()
designations = NodeBuildingConnector("./resource files/campusDesignations.csv")

for row in distances:
    graph.add_vertex(row[0])
    graph.connect_vertex(row[0], row[1], row[2], False)

node_building_tuple = designations.building_lookup('jvd')

if node_building_tuple != False:
    print("true")
    shortest = graph.compute_shortest_path(node_building_tuple[0])
    
