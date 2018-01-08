# http://acm.timus.ru/submit.aspx?space=1&num=1014

def getQforN(n):
  if (n==0):
    return 10
  elif n==1:
    return 1
  else:
    q = 0
    p = 1
    for i in range(9,1,-1):
        while (n%i)==0:
            q += p * i;
            p = p * 10;
            n /= i;
    return [-1,q][n==1]

n = int(input())
print(getQforN(n))