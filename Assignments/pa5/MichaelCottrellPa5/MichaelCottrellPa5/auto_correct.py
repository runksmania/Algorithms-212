#
#Assignment: PA5
#Description: Show use of levenshtein edit distance in a spell checker.
#Author: Michael Cottrell
#HSU ID: 946839472
#Completion Time: 6 hours.
#In completing this program, I received help from the following people:
#N/A
#


from levenshtein import calculate_edit_distance
from dictionary import Dictionary
from heapq import *

#Returns a pq of the possible matches for a given word in the given dictionary.
def find_possible_matches(incorrect_word, dictionary):
  
  possible_matches = []

  if incorrect_word != '':
       
    words = dictionary.lookup_words_starting_with(incorrect_word[0])

    for i in words:
      dist = calculate_edit_distance(incorrect_word, i)

      #Otherwise push into pq the distance and the word.
      heappush(possible_matches, (dist, i))

    if len(incorrect_word) > 1:
      #Repeat earlier step with first two letters in the word.

      words = dictionary.lookup_words_starting_with(incorrect_word[:1])

      for i in words:
        dist = calculate_edit_distance(incorrect_word, i)
        heappush(possible_matches, (dist, i))

      #Now check if first letter was typed incorrectly.

      words = dictionary.lookup_words_starting_with(incorrect_word[1])

      for i in words:
        dist = calculate_edit_distance(incorrect_word, i)
        heappush(possible_matches, (dist, i))

  return possible_matches