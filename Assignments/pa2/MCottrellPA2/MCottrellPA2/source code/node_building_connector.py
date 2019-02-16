from csv_processor import process_csv

class NodeBuildingConnector:
    def __init__(self, file_name):
        designations_array = process_csv(file_name)
        
        self._designations = {}
        
        for row in designations_array:
            
            #Make sure we aren't using info line.
            if row[0] != "Node Name":
                
                #Add the following to the designation hash table.
                #    1. A lookup key which the building code.
                #    2. A tuple containing:
                #        I. The node associated with the building.
                #        II. The name of the building.
                self._designations[row[1]] = (row[0], row[3])
             
    def building_lookup(build_code):
        return self._designations[build_code]
