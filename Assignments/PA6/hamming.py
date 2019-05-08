encoding_matrix = [
  [1,0,0,0,1,1,0],
  [0,1,0,0,1,0,1],
  [0,0,1,0,0,1,1],
  [0,0,0,1,1,1,1]
]

decoding_matrix = [
  [1,0,1,0,1,0,1],
  [0,1,1,0,0,1,1],
  [0,0,0,1,1,1,1]
]

#Function to encode a list of bits into a hamming algorithm.
#Performs matrix multiplication on bits_to_encode and the encoding_matrix.
#Returns a list of bits that is the encoded bits.
def encode(bits_to_encode):

  matrix = [[] for i in range(len(encoding_matrix[0]))]

  if len(bits_to_encode) == len(encoding_matrix):
    for i in range(len(encoding_matrix)):
      l = encoding_matrix[i]

      for j in range(len(l)):
        matrix[j].append(bits_to_encode[i] * l[j])

  print(matrix)
  return [sum(i) % 2 for i in matrix]
