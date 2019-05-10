from hamming import *

test_bits = [0,1,1,0,1,1,1]

par = decode(test_bits)

check_results = parity_check(par)

if check_results == 0:
    print(True)
else:
    test_bits[check_results] = 1 - test_bits[check_results]
    print(test_bits)