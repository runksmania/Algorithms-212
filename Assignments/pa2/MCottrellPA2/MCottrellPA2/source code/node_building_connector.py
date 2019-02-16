from csv_processor import process_csv

class NodeBuildingConnector:
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
             
    def building_lookup(self, build_code):
        build_code = build_code.upper()

        if build_code in self._building_ht:
            return self._building_ht[build_code]

        else:
            return False

    def node_lookup(self, node):

        if node in self._node_building_ht:
            return self._node_building_ht[node]

        else:
            return False