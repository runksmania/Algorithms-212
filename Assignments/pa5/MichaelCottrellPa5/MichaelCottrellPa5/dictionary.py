from trie import Trie
from csv_processor import process_csv

class Dictionary:

  #Constructor
  def __init__(self, file_name):
    
    self._trie_dict = Trie()

    words = process_csv(file_name)

    #Initialize dictionary Trie
    for i in words:
      self._trie_dict.insert_word(i[0])

  #This function calls tree traversal to print words starting with given string.
  def print_words_starting_with(self, string):

    current = self._trie_dict._root

    for i in string:

      if i in current._letters:
        current = current._letters[i]
      else:
        print('none found')
        return
    
    self._trie_dict.tree_traversal_with_print(string, current)


  #This function returns a list of words found by tree_traversal from the given string.
  def lookup_words_starting_with(self, string):

    current = self._trie_dict._root

    for i in string:

      if i in current._letters:
        current = current._letters[i]
      else:
        print('none found')
        return
    
    return self._trie_dict.tree_traversal(string, [], current)


  #This function returns true or false depending on if a given word is found in the trie dictionary.
  def is_word(self, word):

    found = False

    current = self._trie_dict._root

    for i in word:

      if i in current._letters:
        current = current._letters[i]
      else:
        return False

    if current._is_word:
      return True
      
    return found
