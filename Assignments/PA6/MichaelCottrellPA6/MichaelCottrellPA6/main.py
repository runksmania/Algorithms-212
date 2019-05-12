from hamming import decode_data_from_file
from hamming import encode_data_to_file

file_decoded_list = decode_data_from_file('sample.txt.coded')

print(''.join(file_decoded_list), end='')



print('')