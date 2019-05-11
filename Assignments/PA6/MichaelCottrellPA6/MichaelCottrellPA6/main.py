from hamming import *
import struct


correct_corrupted = True
file = open('sample.txt.coded', 'rb').read()
x = struct.unpack("i" * ((len(file) -24) // 4), file[20:-4])

bin_string = []
seven_bit_strings = []

for i in x:
    bin_string.append("{0:b}".format(i))

for i in bin_string:
    lower = 0

    for j in range(1, len(i)):

        if j % 7 == 0:
            temp_list = [int(x) for x in i[lower:j]]

            if len(temp_list) < 7:
                temp_list = reversed(temp_list)
                
                while len(temp_list) < 7:
                    temp_list.append(0)

                temp_list = reversed(temp_list)
            parity_result = -1

            if correct_corrupted:
               parity_result = parity_check(decode(temp_list))
                    
            if parity_result != -1:
                temp_list[parity_result] = 1 - temp_list[parity_result]

            seven_bit_strings.append((temp_list, parity_check(decode(temp_list))))
            lower = j

data = []

for i in range(len(seven_bit_strings) - 1):
    string = seven_bit_strings[i][0]
    string2 = seven_bit_strings[i + 1][0]

    temp_data = []

    temp_data.append(str(string[2]))
    temp_data.append(''.join([str(i) for i in string[4:]]))
    temp_data.append(str(string2[2]))
    temp_data.append(''.join([str(i) for i in string2[4:]]))

    data.append(''.join(temp_data))

chars = [chr(int(i, 2)) for i in data]

print('done')