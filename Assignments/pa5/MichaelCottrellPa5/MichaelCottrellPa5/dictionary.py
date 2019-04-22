from trie import Trie
from csv_processor import process_csv

class Dictionary:

  def __init__(self, file_name):
    self._trie_dict = Trie()

    words = process_csv(file_name)
  
    for i in words:
      self._trie_dict.insert_word(i[0])

  def print_words_starting_with(self, string):

    current = self._trie_dict._root

    for i in string:

      if i in current._letters:
        current = current._letters[i]
      else:
        print('none found')
        return
    
    self._trie_dict.tree_traversal_with_print(string, current)

  def lookup_words_starting_with(self, string):

    current = self._trie_dict._root

    for i in string:

      if i in current._letters:
        current = current._letters[i]
      else:
        print('none found')
        return
    
    return self._trie_dict.tree_traversal(string, [], current)

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
