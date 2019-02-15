import csv
from graph import Graph


def process_csv(file_name):
    data = []
    
    with open(file_name, 'r') as some_file:
        csv_file = csv.reader(some_file, delimiter=',', quotechar='"')

        for row in csv_file:
            data.append(row)

    return data

result = process_csv("./resource files/distances.csv")
graph = Graph()

for row in result:
    graph.add_vertex(row[0])
    graph.connect_vertex(row[0], row[1], row[2], False)

shortest = graph.compute_shortest_path('A');

for i in shortest:
    print(i + ": " + str(shortest[i][0]))
    
    if shortest[i][1] == "":
        print("Path: None")
    else:
        print("Path: " + shortest[i][1])
