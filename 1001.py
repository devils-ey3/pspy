# http://acm.timus.ru/problem.aspx?space=1&num=1001

# Test case
# Stdin
#  1427  0   
 
#     876652098643267843 
#  5276538

# Stdout

# 2297.0716
# 936297014.1164
# 0.0000
# 37.7757


from sys import stdin
from re import findall,M
from math import sqrt

data = stdin.readlines()
data = ' '.join(data)
digits = findall('(\d+)',data,M)
for numbers in digits[::-1]:
	print('%.4f' %sqrt(int(numbers)))