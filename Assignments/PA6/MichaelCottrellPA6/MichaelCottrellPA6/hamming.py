encoding_matrix = [
    [1,0,0,0,1,1,0],
    [0,1,0,0,1,0,1],
    [0,0,1,0,0,1,1],
    [0,0,0,1,1,1,1]]

decoding_matrix = [
    [1,0,1,0,1,0,1],
    [0,1,1,0,0,1,1],
    [0,0,0,1,1,1,1]]

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

    return [sum(i) % 2 for i in matrix]

#Function to decode a list of bits encoded by a hamming algorithm.
#Performs matrix multiplication on bits_to_decode and the decoding_matrix
#Returns a list of bits that can indicated corrupted bit or if no corruptions found.
def decode(bits_to_decode):

    matrix = [[] for i in range(len(decoding_matrix))]

    if len(decoding_matrix[0]) == len(bits_to_decode):
        for i in range(len(decoding_matrix)):
            l = decoding_matrix[i]

            for j in range(len(l)):
                matrix[i].append(bits_to_decode[j] * l[j])

    return [sum(i) % 2 for i in matrix]

#Function to check if the bits are correct or have been corrupted.
#Returns a -1 if the bits are not corrupted, and returns the error bit for a list indexed by 0 if corrupted.
def parity_check(bits_decoded):

    if sum(bits_decoded) == 0:
        return -1

    else:
        wrong_bit = 0

        for i in range(len(bits_decoded)):
            if bits_decoded[i] == 1:
                wrong_bit += pow(2, i)
        
        return wrong_bit - 1   
    