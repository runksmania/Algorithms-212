#
#Assignment: PA2
#Description: Perform and analyze Dijkstra's shortest path algorithm with the HSU Campus.
#Author: Michael Cottrell
#HSU ID: 946839472
#Completion Time: 5 hours.
#In completing this program, I received help from the following people:
#N/A
#

from csv_processor import process_csv

class NodeBuildingConnector:

    #Constructor
    #Creates two hash tables from a csv file that has the relationship between buildings and nodes.
    #Time Complexity: O(N)
    #Space Complexity: O(N)
    #N = number of lines in the csv
    def __init__(self, file_name):
        designations_array = process_csv(file_name)
        
        self._building_ht = {}
        self._node_building_ht = {}
        
        for row in designations_array:
            #The row has three elements:
            #    1. Node name.
            #    2. HSU Bulding Code.
            #    3. Bulding full name.

            #Make sure we aren't using info line.
            if row[0] != "Node Name":
                
                #Add the following to the designation hash table.
                #    1. A lookup key which the building code.
                #    2. A tuple containing:
                #        I. The node associated with the building.
                #        II. The name of the building.
                self._building_ht[row[1]] = (row[0], row[2])
                
                #Check if node already exists in node_building_ht.
                if not row[0] in self._node_building_ht:

                    #If it doesnt exist add it and its value is an array of buildings.
                    #Instatiate the array with this building.
                    self._node_building_ht[row[0]] = [row[2]]

                else:
                    #If it does exist append the array with the buildling.
                    self._node_building_ht[row[0]].append(row[2])
             
    #Looks up the building code and returns a tuple if found false if not found.
    #Time Complexity: O(1)
    #Space Complexity: O(1)
    def building_lookup(self, build_code):
        build_code = build_code.upper()

        if build_code in self._building_ht:
            return self._building_ht[build_code]

        else:
            return False

    #Looks up buildings connected to a node.  Returns a list if found false if not found.
    #Time Complexity: O(1)
    #Space Complexity: O(1)
    def node_lookup(self, node):

        if node in self._node_building_ht:
            return self._node_building_ht[node]

        else:
            return False