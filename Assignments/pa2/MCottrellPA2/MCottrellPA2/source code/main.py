from csv_processor import process_csv
from graph import Graph
from node_building_connector import NodeBuildingConnector

distances = process_csv("./resource files/distances.csv")
graph = Graph()
designations = NodeBuildingConnector("./resource files/campusDesignations.csv")

for row in distances:
    graph.add_vertex(row[0])
    graph.connect_vertex(row[0], row[1], row[2], False)

shortest = graph.compute_shortest_path('A');

for i in shortest:
    print(i + ": " + str(shortest[i][0]))
    
    if shortest[i][1] == "":
        print("Path: None")
    else:
        print("Path: " + shortest[i][1])
