from hamming import *
import struct

correct_corrupted = True
array_of_bytes = []

with open('sample.txt.coded', 'rb') as file:

    #Read first btye
    byte = file.read(1)

    while byte != b'':
        #While btyes read are not empty.

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

        if correct_corrupted:
            if parity != -1:
                
                #If user wants bits corrected, and a bit is corrupted fix it.
                byte_array[parity] = 1 - byte_array[parity]

        #Append the byte array and its parity potentially after fixing to the array of bytes.
        #Appending parity here is not necessary but is done for debugging purposes.
        array_of_bytes.append((byte_array, parity_check(decode(byte_array))))

        #Read next byte
        byte = file.read(1)

#binary_chars is used for debugging purposes.
binary_chars = []
chars = []

for i in range(len(array_of_bytes) - 1):
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

for i in range(len(chars)):
    
    if i % 2 == 0:
        
        #For some reason the characters we want are actually every other character.
        print(chr(int(binary_chars[i], 2)), end='')

print('\n')