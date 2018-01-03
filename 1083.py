# Timus problem solution 1083
# http://acm.timus.ru/forum/?space=1&num=1083

##Test case
##1) 11 !!!! - 231
##2) 13 !! - 135135
##3) 36 !!!!!! - 33592320
##4) 7 !!!!! - 14
##5) 21 !!!!!!! - 2058


inp = input().split()
number = int(inp[0])
increase = len(inp[1])
result = 1
for x in range(0,number,increase):
        result *= number - x
print(result)
