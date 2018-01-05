# Problem 1209. 1, 10, 100, 1000...
# http://acm.timus.ru/problem.aspx?space=1&num=1209

# See the sequence
# 1
# 10
# 100
# 1000
# 10000
# 100000

# We get '1' after a '0' increased

# The sequence of getting '1' is 1,2,4,7,11,16 and so on

# if we multiple a number by 8 and subtrack by 7 and the result
# of the equation can be sqrt without getting fractional value
# then the position is 1. 

# like (8*7)-7 = 56-7 = 49
# √49 = 7.0 
# so we get no fractonal number 


from math import modf,sqrt

def checkOne(num):
	if modf(sqrt((8*num)-7))[0]==0:
		return '1 '
	else:
		return '0 '


result = ''

for x in range(int(input())):
    result+=checkOne(int(input()))

print(result.lstrip())