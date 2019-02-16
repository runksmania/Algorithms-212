import csv

def process_csv(file_name):
    data = []
    
    with open(file_name, 'r') as some_file:
        csv_file = csv.reader(some_file, delimiter=',', quotechar='"')

        for row in csv_file:
            data.append(row)

    return data
