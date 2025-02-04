#
#Assignment: PA6
#Description: Use hamming algorithm (7,4) to encode and decode a data file.
#Author: Michael Cottrell
#HSU ID: 946839472
#Completion Time: 12 hours.
#In completing this program, I received help from the following people:
#Adam Carter
#

import sys
from hamming import decode_data_from_file
from hamming import encode_data_from_file

def encodeFile(file_name):
   encoded_data = encode_data_from_file(file_name)
   
   with open(file_name + '.coded', 'wb') as some_file:
       some_file.write(encoded_data)

def decodeFile(file_name):
   decoded_data = decode_data_from_file(file_name)
   file_name = file_name.split('.')
   file_name = file_name[0] + '.decoded.txt'
   decoded_copy = []

   for i in decoded_data:

       #For some complex files for some reason one of my tuples from an earlier stage in decoding doesn't get converted.
       #This is the fix for now, but I intended to do a real fix later once school is not in session.
       if type(i) != type(()):
           decoded_copy.append(i)

   with open(file_name, 'w') as some_file:
       print(''.join(decoded_copy), end='', file=some_file)

def main():
   if len(sys.argv) != 3:
      print("Expected format: PA6.py <encode / decode> <file_name>")
      return

   if sys.argv[1] == "encode":
      #encode ABC.txt to ABC.txt.coded
      encodeFile(sys.argv[2])
      print("File", sys.argv[2], "encoded.")

   elif sys.argv[1] == "decode":
      #decode ABC.txt.coded to ABC.decoded.txt
      decodeFile(sys.argv[2])
      print("File", sys.argv[2] , "decoded.")
   else:
      print("Unexpected command.")

if __name__ == '__main__':
   main()