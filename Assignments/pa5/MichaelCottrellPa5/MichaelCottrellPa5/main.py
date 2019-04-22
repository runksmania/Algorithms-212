from dictionary import Dictionary

dictionary = Dictionary('resourceFiles/words.txt')

dictionary.print_words_starting_with('ph')

li = dictionary.lookup_words_starting_with('ph')

for i in li:
  print(i)
