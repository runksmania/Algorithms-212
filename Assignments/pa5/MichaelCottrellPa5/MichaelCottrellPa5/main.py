from dictionary import Dictionary
from auto_correct import find_possible_matches
from heapq import heappop

dictionary = Dictionary('resourceFiles/words.txt')

#li = dictionary.lookup_words_starting_with('this')

#for i in li:
 # print(i)

li = find_possible_matches('philosoph', dictionary)

ten_closest_matches = []

while len(ten_closest_matches) < 10:
  top = heappop(li)

  if top[1] not in ten_closest_matches:
    ten_closest_matches.append(top[1])

for i in ten_closest_matches:
  print(i)