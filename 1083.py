# Timus problem solution 1083
# http://acm.timus.ru/forum/?space=1&num=1083

inp = input().split()
number = int(inp[0])
increase = len(inp[1])
result = 1
print(number, increase)
for x in range(0,number,increase):
        result *= number - x
print(result)
