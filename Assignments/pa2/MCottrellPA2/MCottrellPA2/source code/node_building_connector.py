from csv_processor import process_csv

class NodeBuildingConnector:
    def __init__(self, file_name):
        self._designations = process_csv(file_name)