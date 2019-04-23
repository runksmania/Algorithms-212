#
#Assignment: PA5
#Description: Show use of levenshtein edit distance in a spell checker.
#Author: Michael Cottrell
#HSU ID: 946839472
#Completion Time: 6 hours.
#In completing this program, I received help from the following people:
#N/A
#


import csv

#Function to process a csv file and return a list of thse lines of data.
#Time Complexity: O(N)
#Space Complexity: O(N) 
#N = number of lines in csv file.
def process_csv(file_name):
    data = []
    
    with open(file_name, 'r') as some_file:
        csv_file = csv.reader(some_file, delimiter=',', quotechar='"')

        for row in csv_file:
            data.append(row)

    return data
