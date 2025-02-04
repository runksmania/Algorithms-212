#
#Assignment: PA5
#Description: Show use of levenshtein edit distance in a spell checker.
#Author: Michael Cottrell
#HSU ID: 946839472
#Completion Time: 6 hours.
#In completing this program, I received help from the following people:
#N/A
#


from trie_node import Trie_Node

class Trie:

  def __init__(self):
    self._root = Trie_Node()
  
  def insert_word(self, word):

    #Create a current pointer
    current = self._root
    for i in word:
      
      if i in current._letters:
        current = current._letters[i]
      else:
        current._letters[i] = Trie_Node()
        current = current._letters[i]
      
    current._is_word = True

  #This function is mainly used for debugging the trie.
  #Prints words found in the Trie.
  def tree_traversal_with_print(self, string, node):

    if node._is_word:
      print(string)

    if node._letters:

      for k,v in node._letters.items():
        current_string = string + k
        self.tree_traversal_with_print(current_string, v)
        
  #Returns a list of words found in the Trie.
  def tree_traversal(self, string, list, node):

    if node._is_word:
      list.append(string)

    if node._letters:

      for k,v in node._letters.items():
        current_string = string + k
        list = self.tree_traversal(current_string, list, v)

    return list