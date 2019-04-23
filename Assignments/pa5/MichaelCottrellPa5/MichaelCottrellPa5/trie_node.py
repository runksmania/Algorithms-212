#
#Assignment: PA5
#Description: Show use of levenshtein edit distance in a spell checker.
#Author: Michael Cottrell
#HSU ID: 946839472
#Completion Time: 6 hours.
#In completing this program, I received help from the following people:
#N/A
#


class Trie_Node:

  def __init__(self):
    self._letters = {}
    self._is_word = False
