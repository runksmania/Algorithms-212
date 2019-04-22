from heapq import heappop
from dictionary import Dictionary
from auto_correct import find_possible_matches
from csv_processor import process_csv

def print_corrections(word, context, possible_matches):

  print('Uknown word: ' + word)
  print('Context:\n' + context + '\n')
  print('Possible corrections:')
  print('1. None of the following are correct.')

  for i in range(len(possible_matches)):
    print(str(i + 2) + '. ' + possible_matches[i])

dictionary = Dictionary('resourceFiles/words.txt')
previous_corrections = process_csv('resourceFiles/previous_corrections.csv')
previous_corrections_dict = {}

for i in previous_corrections:
  if i:
    #Make sure list is not empty.
    previous_corrections_dict[i[0]] = [j for j in i[1].split(',')]

print('Autocorrect Program Initiated.')
print('All input files will assumed to be in the resourceFiles directory.')
print('All output files will be put in the outputFiles directory.\n')
file_to_check = input('Please input a file to autocorrect: ')
output_file_name = input('Please input a filename to output to: ')
print()

file = open('resourceFiles/' + file_to_check, 'r').readlines()
output_list = []

for i in file:

  current_corrected_line = []

  for j in i.split():
    
    if j[-1] in ',.?!;:':  

      #Remove punctuation for search
      word = j[:-1]

      if not dictionary.is_word(word):

        top_ten_matches = []

        if word not in previous_corrections_dict:
          #If we have not encountered this before, search for possible corrections and print top 10.
          possible_matches = find_possible_matches(word, dictionary)

          while len(top_ten_matches) < 10:
            top = heappop(possible_matches)[1]

            if top not in top_ten_matches:
              top_ten_matches.append(top)

          print_corrections(word, i, top_ten_matches)
        
        else:
          print_corrections(word, i, previous_corrections_dict[word])
          top_ten_matches = previous_corrections_dict[word]
          
        selection = input('Enter a selection: ')

        while selection.isalpha() or int(selection) > 11 or int(selection) < 1:
          print('\nIncorrect selection. Please try again.')

        if selection == '1':
          #If our corrections didn't match the correct word get the users input for correct word.
          #Then add it and our possible corrections to the previously seen.
          correction = input('Please enter the correct spelling: ')
          previous_corrections_dict[word] = [correction] + top_ten_matches
          print()

        else:
          #Due to print formatting selection will be 2 higher than our list index.
          sel = int(selection) - 2

          #Make selected correction the first entry.
          #Then add to previously seen.
          correction = top_ten_matches[int(sel)]
          top_ten_matches[int(sel) - 1] = top_ten_matches[0]
          top_ten_matches[0] = correction
          previous_corrections_dict[word] = top_ten_matches

      j = word + j[-1]
    
    else:
      if not dictionary.is_word(j):

        top_ten_matches = []

        if j not in previous_corrections_dict:
          #If we have not encountered this before, search for possible corrections and print top 10.
          possible_matches = find_possible_matches(j, dictionary)

          while len(top_ten_matches) < 10:
            top = heappop(possible_matches)[1]

            if top not in top_ten_matches:
              top_ten_matches.append(top)

          print_corrections(j, i, top_ten_matches)

        else:
          print_corrections(j, i, previous_corrections_dict[j])
          top_ten_matches = previous_corrections_dict[j]

        selection = input('Enter a selection: ')

        while selection.isalpha() or int(selection) > 11 or int(selection) < 1:
          print('\nIncorrect selection. Please try again.')
          selection = input('Enter a selection: ')

        if selection == '1':
          #If our corrections didn't match the correct word get the users input for correct word.
          #Then add it and our possible corrections to the previously seen.
          correction = input('Please enter the correct spelling: ')
          previous_corrections_dict[j] = [correction] + top_ten_matches
          j = correction
          print()

        else:
          #Due to print formatting selection will be 2 higher than our list index.
          sel = int(selection) - 2

          #Make selected correction the first entry.
          #Then add to previously seen.
          correction = top_ten_matches[int(sel)]
          top_ten_matches[int(sel)] = top_ten_matches[0]
          top_ten_matches[0] = correction
          previous_corrections_dict[j] = top_ten_matches
          j = correction


    current_corrected_line.append(j)
    
  output_list.append(current_corrected_line)

with open('outputFiles/' + output_file_name, 'w') as some_file:
  
  for i in output_list:
    print(' '.join(i), file=some_file)

with open('resourceFiles/previous_corrections.csv', 'w') as prev_corrections_file:
  for k,v in previous_corrections_dict.items():
    print(','.join([k, '"' + ','.join(v) + '"']), file=prev_corrections_file)

print('Corrected output file has been created.')