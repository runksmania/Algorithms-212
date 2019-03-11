#
#Assignment: PA3
#Description: Perform and analyze min span trees with Dijkstra's shortest path
#algorithm.
#Author: Michael Cottrell
#HSU ID: 946839472
#Completion Time: 5 hours.
#In completing this program, I received help from the following people:
#N/A
#
import sys
from csv_processor import process_csv
from graph import Graph
from heapq import *

print('***Route Planner***')
print('*Note all input files will assumed to be in the /resourceFiles directory.\n*Enter the file name only.\n')
map_data = process_csv('resourceFiles/' + input('Enter map file: '))
delivery_data = process_csv('resourceFiles/' + input('Enter delivery file: '))

g = Graph()
deliveries = {}

#Create a dictionary containing our nodes for the min span tree.
for i in delivery_data:
  deliveries[i[0]] = 0

#Create Graph
for i in map_data:
  g.add_vertex(i[0])
  g.connect_vertex(i[0], i[1], i[2], True)

#Setup variables for optimized path.
total_time = sys.maxsize
path = {}
start = ''

#Try each starting point in our list of nodes for delivery min span tree.
for i in delivery_data:

    #Setup variables to run dijkstra for i as starting node.
    current_start = i[0]
    delivery_current = deliveries.copy()
    delivery_current[current_start] = 1
    current = current_start
    delivery_time = 0
    current_path = {}

    #While we have not reached every min span tree node.
    while len(current_path) < len(delivery_current) - 1:

        closest = g.shortest_path_dict_nodes(current, delivery_current)
    
        if closest != 0:

            #Add time to total time for this path.
            delivery_time += closest[0]

            #Insert a tuple containing path time to next node, and path.
            current_path[current] = (closest[0], closest[1][1])

            #Change new start node for next dijkstra's run.
            current = closest[1][0]

            #Mark node as visited.
            delivery_current[current] = 1
        else:
            
            #Something went wrong if nothing was found.
            break
  
    if delivery_time < total_time:
        
        #If This path is the current most optimized copy to variables.
        total_time = delivery_time
        path = current_path
        start = current_start
  

print('\nTotal transit time: ' + str(total_time) + ' minutes')
print('Complete Route:\n\nTime to first desination: ' + str(path[start][0]) + ' minutes\nRoute: ' + start + ' -> ' + ' -> '.join(path[start][1].split()))
for i in path:
    if i != start:
        print('Time to next desination: ' + str(path[i][0]) + ' minutes\nRoute: ' + i + ' -> ' + ' -> '.join(path[i][1].split()) + '\n')
