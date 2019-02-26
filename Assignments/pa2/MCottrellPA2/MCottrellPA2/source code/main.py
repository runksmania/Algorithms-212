#
#Assignment: PA2
#Description: Perform and analyze Dijkstra's shortest path algorithm with the HSU Campus.
#Author: Michael Cottrell
#HSU ID: 946839472
#Completion Time: 5 hours.
#In completing this program, I received help from the following people:
#N/A
#

from math import floor
from random import *
from csv_processor import process_csv
from graph import Graph
from node_building_connector import NodeBuildingConnector

distances = process_csv('./resource files/distances.csv')
graph = Graph()
designations = NodeBuildingConnector('./resource files/campusDesignations.csv')

for row in distances:
    graph.add_vertex(row[0])
    graph.connect_vertex(row[0], row[1], row[2], False)

print('****HSU transit time calculator****')

restart_search_loop = True

while restart_search_loop:

    restart_search_loop = False
    start = input('Enter starting location: ').upper()
    destination = input('Enter destination: ').upper()
    node_building_tuple = designations.building_lookup(start)
    end_node = designations.building_lookup(destination)

    if node_building_tuple != False and end_node != False:

        end_node = designations.building_lookup(destination)[0]
        shortest = graph.compute_shortest_path(node_building_tuple[0])
        minutes = floor((shortest[end_node][0] / 60))
        seconds = floor((shortest[end_node][0] - minutes * 60))
        print('Estimated travel time: ' + str(minutes) + ' minutes and ' + str(seconds) + ' seconds')
        print('On your way from ' + start + ' to ' + destination + ' you will pass: ')
        buildings_passed = []

        #Loop through each node in the path part of the tuple.
        for node in shortest[end_node][1].split():

            #Get the list of buildings in that node.
            building_list = designations.node_lookup(node)
            rand = Random()
            rand.seed()
            buildings_passed.append(building_list[randint(0, len(building_list) - 1)])
            #Output a random building from the list.
        
        print(', '.join(buildings_passed))
        print()

    else:
        print('No buildings found matching your search parameters.\n')

    check_continue = input('Do you want to search again? Typing anything continues:')

    if len(check_continue) != 0:
        restart_search_loop = True

