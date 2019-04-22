class Trie_Node:

  def __init__(self):
    self._letters = {}
    self._is_word = False

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

  def tree_traversal(self, string, node):

    if node._is_word:
      print(string)

    if node._letters:

      for k,v in node._letters.items():
        current_string = string + k
        self.tree_traversal(current_string, v)


  def print_word_starting_with(self, letter):

    if letter == '':
      for k,v in self._root._letters.items():
        self.tree_traversal(k, v)
    else:
      self.tree_traversal(letter, self._root._letters[letter])
