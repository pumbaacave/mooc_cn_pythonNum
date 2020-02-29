def fac(n):
    intNum = 0
    ## check if n can be divided by i
    for i in range(1, n):
        if (n % i == 0):
            intNum += i
    return intNum
   
def findFrindsNum(n):
    for i in range(2, n):
        ingreSum = fac(i)
        if ingreSum > i and ingreSum < n and fac(ingreSum) == i:
            print('{0}-{1}'.format(i, ingreSum))

import time

n = int(input())
start = time.time()
findFrindsNum(n)
print(time.time()-start, 's')
