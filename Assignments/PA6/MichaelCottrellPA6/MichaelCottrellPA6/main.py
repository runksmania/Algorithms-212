import sys
from hamming import decode_data_from_file
from hamming import encode_data_to_file

def encodeFile(file_name):
   encode_data_to_file(file_name)

def decodeFile(file_name):
   decoded_data = decode_data_from_file(file_name)
   file_name = file_name.split('.')
   file_name = file_name[0] + '.decoded.txt'

   with open(file_name, 'w') as some_file:
       print(''.join(decoded_data), end='', file=some_file)

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