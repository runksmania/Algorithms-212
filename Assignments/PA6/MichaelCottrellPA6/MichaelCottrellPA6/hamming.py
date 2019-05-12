encoding_matrix = [
    [1,1,1,0,0,0,0],
    [1,0,0,1,1,0,0],
    [0,1,0,1,0,1,0],
    [1,1,0,1,0,0,1]]

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
#Returns a list of bits that can indicated corrupted bit or if no corruptions
#found.
def decode(bits_to_decode):

    matrix = [[] for i in range(len(decoding_matrix))]

    if len(decoding_matrix[0]) == len(bits_to_decode):
        for i in range(len(decoding_matrix)):
            l = decoding_matrix[i]

            for j in range(len(l)):
                matrix[i].append(bits_to_decode[j] * l[j])

    return [sum(i) % 2 for i in matrix]

#Function to check if the bits are correct or have been corrupted.
#Returns a -1 if the bits are not corrupted, and returns the error bit for a
#list indexed by 0 if corrupted.
def parity_check(bits_decoded):

    if sum(bits_decoded) == 0:
        return -1

    else:
        wrong_bit = 0

        for i in range(len(bits_decoded)):
            if bits_decoded[i] == 1:
                wrong_bit += pow(2, i)
        
        return wrong_bit - 1   

def encode_data_from_file(file_name):    
  file_data_half_bytes = []

  with open(file_name, 'r') as some_file:
    char = some_file.read(1)

    while char != '':
      
      if char != '\n' and char != '\r':
        #Get binary string skipping 0b part of string.
        byte = bin(ord(char))[2:]

        #Add 0's to the front of the binary string if less than 8 bits long.
        byte = '0' * (8 - len(byte)) + byte

        byte_half_1 = [int(i) for i in byte[:4]]
        byte_half_2 = [int(i) for i in byte[4:]]
        
        file_data_half_bytes.append(byte_half_1)
        file_data_half_bytes.append(byte_half_2)
      
      else:
        
        if char == '\n':
          file_data_half_bytes.append('\n')

      char = some_file.read(1)

  encoded_data = bytearray()

  for i in file_data_half_bytes:

      if i != '\n':
          encoded = encode(i)
          binary_string = '0b0' + ''.join([str(j) for j in encoded])
          encoded_data.append(int(binary_string, 2))
      
      else:
          encoded_data.append(ord(i))
          encoded_data.append(ord('\r'))
        
  return encoded_data
    
#Function to decode a hamming encoded binary file.
#Returns a list of characters which is the decoded file.
def decode_data_from_file(file_name):

    array_of_bytes = []
    bytes = []
    asked_for_corrections = False
    correct_corrupted = False


    with open(file_name, 'rb') as file:

        #Read first btye
        byte = file.read(1)

        while byte != b'':
            #While btyes read are not empty.
            if byte != b'\r' and byte != b'\n':

                bytes.append((byte, bin(ord(byte))))

                #Convert byte into binary string without 0b, and insert 1's and 0's into list.
                byte_string = bin(ord(byte))[2:]
                byte_array = [int(i) for i in byte_string]

                #If the size of the binary string was less than 7 we need to add 0's to the front.
                #This is due to python removing 0's in front of a binary number.
                if len(byte_array) < 7:
                    byte_array = list(reversed(byte_array))

                    while len(byte_array) < 7:
                        byte_array.append(0)

                    byte_array = list(reversed(byte_array))

                parity = parity_check(decode(byte_array))

                #If parity is not -1 a bit has been corrupted.
                if parity != -1:

                    if not asked_for_corrections:
                        user_input = input('Do you want to correct potential corrupted bits?\n'
                         + '**Warning correction corrupted bits may still result in incorrect data.**\nEnter (Y)es or (N)o: ')
                        asked_for_corrections = True
                        print()

                        if user_input.lower() == 'y':
                            correct_corrupted = True
                
                    #If user wants bits corrected, and a bit is corrupted fix it.
                    if correct_corrupted:
                        byte_array[parity] = 1 - byte_array[parity]

                #Append the byte array and its parity potentially after fixing to the array of bytes.
                #Appending parity here is not necessary but is done for debugging purposes.
                array_of_bytes.append((byte_array, parity_check(decode(byte_array))))

            else:
            
                if byte == b'\n':
                    array_of_bytes.append('\n')

            #Read next byte
            byte = file.read(1)

    #binary_chars is used for debugging purposes.
    binary_chars = []
    chars = []

    for i in range(0, len(array_of_bytes) - 1, 2):

        if array_of_bytes[i] != '\n' and array_of_bytes[i + 1] != '\n':
            combined_bytes = []

            #Each byte only contains 4 of the 8 bits for an ascii character.
            #So we need to grab 2 at a time.
            data_1 = array_of_bytes[i][0]
            data_2 = array_of_bytes[i + 1][0]

            #Append the data bits from first byte.
            combined_bytes.append(str(data_1[2]))
    
            for j in range(4, 7):
                combined_bytes.append(str(data_1[j]))

            #Append data bits from second byte.
            combined_bytes.append(str(data_2[2]))
    
            for j in range(4, 7):
                combined_bytes.append(str(data_2[j]))

            #Join combined_bytes with 0b so python can properly convert to an int and then a character.
            #Binary_chars is appending binary string for debugging purposes.
            binary_chars.append('0b' + ''.join(combined_bytes))
            chars.append(chr(int('0b' + ''.join(combined_bytes), 2)))
    
        else:

            for j in range(i, i + 2):
                
                if type(array_of_bytes[j]) == type('\n'):
                    chars.append(array_of_bytes[i])

    return chars
