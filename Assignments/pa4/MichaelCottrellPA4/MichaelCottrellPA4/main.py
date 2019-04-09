#for CSV parsing
import csv
from math import log2

class TreeNode:
   def __init__(self):
      self.children = {}
      self.value = ""

def process_csv(file_name):
   data = []
   with open(file_name, 'r') as some_file:
      csv_file = csv.reader(some_file, 
                            delimiter=',', 
                            quotechar='"')
      for row in csv_file:
         data.append(row)
      return data

def calculate_entropy(outcome_levels):
   denominator = 0.0
   for key in outcome_levels:
      denominator += outcome_levels[key]
   
   entropy = 0.0
   for key in outcome_levels:
      ratio = outcome_levels[key] / denominator
      logged = log2(ratio)
      entropy += -ratio * logged
   return entropy

def build_frequency_distribution(sequence):
   distribution = {}
   for item in sequence:
      if not item in distribution:
         distribution[item] = 0
      distribution[item] += 1
   return distribution

def get_observations(matrix, column):
   result = []
   for i in range(len(matrix)):
      result.append(matrix[i][column])
   return result

def reduce_matrix(matrix, column, predictor):
   result = []
   for i in range(len(matrix)):
      if matrix[i][column] == predictor:
         result.append(matrix[i])
   return result

def find_max_gain(matrix, outcome_column, entropy):
   if len(matrix) == 0:
      return -1
   
   information_gain = []
   for column in range(len(matrix[0])):
      if column == outcome_column:
         information_gain.append(-1)
         continue
      observations = get_observations(matrix, column)
      observation_levels = build_frequency_distribution(observations)
      local_entropy = 0.0
      for level in observation_levels:
         reduced_matrix = reduce_matrix(matrix, column, level)
         reduced_observations = get_observations(reduced_matrix, outcome_column)
         local_entropy += observation_levels[level] / len(observations) * calculate_entropy(build_frequency_distribution(reduced_observations))
      information_gain.append(entropy - local_entropy)
   
   most_gain = 0
   for i in range(1, len(information_gain)):
      if information_gain[i] > information_gain[most_gain]:
         most_gain = i
   return most_gain

def build_tree(matrix, predictors, outcome_column):
   observations = get_observations(matrix, outcome_column)
   entropy = calculate_entropy(build_frequency_distribution(observations))
   if(entropy < 0.01):
      node = TreeNode()
      node.value = matrix[0][outcome_column]
      return node
   
   col = find_max_gain(matrix, outcome_column, entropy)
   node = TreeNode()
   node.value = predictors[col]

   selected_observations = get_observations(matrix, col)
   selected_levels = build_frequency_distribution(selected_observations)
   for level in selected_levels:
      reduced_matrix = reduce_matrix(matrix, col, level)
      node.children[level] = build_tree(reduced_matrix, predictors, outcome_column)
   return node
    
def tree_to_array_helper(node, tree_array):

    #Add this nodes children and then call its children.
    for key in node.children:
        string_array = []
        string_array.append(key)
        string_array.append(node.children[key].value)
        string_array.append(str(len(node.children[key].children)))
        tree_array.append('|'.join(string_array))

    for key in node.children:
        tree_to_array_helper(node.children[key], tree_array)

    return tree_array

def tree_to_array(root, tree_array):

    #setup the array with the root
    string_array = []
    string_array.append('NULL')
    string_array.append(root.value)
    string_array.append(str(len(root.children)))
    tree_array.append('|'.join(string_array))

    #Add the three children.
    for key in root.children:
        string_array = []
        string_array.append(key)
        string_array.append(root.children[key].value)
        string_array.append(str(len(root.children[key].children)))
        tree_array.append('|'.join(string_array))

    #Call the recursive helper on the children.
    for key in root.children:
        tree_to_array_helper(root.children[key], tree_array)

    return tree_array

def write_tree_to_file(tree_array, file_name):
    
    with open(file_name, 'w') as some_file:
        
        for i in tree_array:
            print(i, file=some_file)

def build_tree_from_tree_array_helper(node, tree_array, count, child_pos):

    #Insert all the children into the current node.
    first = tree_array[count].split('|')

    for i in range(int(first[2])):
        data = tree_array[child_pos + i].split('|')
        node.children[data[0]] = TreeNode()
        node.children[data[0]].value = data[1]

    count += 1

    #Recursively call its children and show the place they are in the array.
    for i in range(len(node.children)):
        data = tree_array[child_pos + i].split('|')
        build_tree_from_tree_array_helper(node.children[data[0]],  tree_array, count, child_pos + int(first[2]) + int(data[2]))

    return node
        

def build_tree_from_tree_array(tree_array):
    
    #Setup the root
    count = 0
    child_pos = count + 1
    root = TreeNode()
    first = tree_array[count].split('|')
    root.value = first[1]

    #Add its children.
    for i in range(child_pos, int(first[2]) + child_pos):
        data = tree_array[i].split('|')
        root.children[data[0]] = TreeNode()
        root.children[data[0]].value = data[1]

    count += 1
    child_num = 0

    #Recursively call its children to add their children.
    #Noting the position they start and skipping those without children.
    for i in range(len(root.children)):
        data = tree_array[child_pos + i].split('|')
        
        if int(data[2]) != 0:
            build_tree_from_tree_array_helper(root.children[data[0]],  tree_array, count, child_pos + child_num + int(first[2]))
        child_num += 1

    return root

def read_tree_from_file(file_name):
    
    #Read File
    tree_array = open(file_name, 'r').readlines()

    #Get rid of '/n' characters
    for i in range(len(tree_array)):
        tree_array[i] = tree_array[i][:-1]

    return build_tree_from_tree_array(tree_array)



def main():
   
   option = ''
   root = TreeNode()
   header = []
   result = []

   while not (option == '1' or option == '2'):
         print('Please enter the number for one of the following options:\n' 
               + '1. Build decision tree from file\n' 
               + '2. Read decision tree from file'
               )
         option = input('Enter a choice: ')
         print()

   if option == '1':
       file_name = input('Note the file must be in the resourceFiles directory.\nPlease enter a filename: ')
       outcome_column = int(input('Please enter the output column number: '))
       #result = process_csv("resourceFiles/" + file_name)
       result = process_csv("resourceFiles/easy data set.csv")
       header = result[0]
       result = result[1:]
       root = build_tree(result, header, 4)
   else:
        file_name = input('Note the file must be in the resourceFiles directory.\nPlease enter a filename: ')
        root = read_tree_from_file(file_name)


   option = ''
   while not (option == '1' or option == '2' or option == '3'):
       print('\n\nPlease enter the number for one of the following options:\n' 
               + '1. Write decision tree to file\n' 
               + '2. Write data to file with prediction'
               + '3. Exit.'
               )
       option = input('Enter a choice: ')
       print()

   file_name = input('Enter a file name to write to: ')
   print()       

   if option == '1':
       tree_array = tree_to_array(root, [])
       write_tree_to_file(tree_array, file_name)
   elif option == '2':
       print('awesome')


   print("done")

if __name__ == '__main__':
   main()