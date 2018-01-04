# Timus problem solution 1086
# http://acm.timus.ru/problem.aspx?space=1&num=1086

from math import sqrt
def getList(maxNumber):
    primeLst = []
    for num in range(2,1500000):
        if all(num%i!=0 for i in range(2,int(sqrt(num))+1)):
           primeLst.append(num)
           if len(primeLst)==maxNumber:
                return primeLst

lst = []
for x in range(int(input())):
    lst.append(int(input()))
primeNumbers = getList(max(lst[1::]))
for x in lst:
    print(primeNumbers[x-1])