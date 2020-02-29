import time
# define if number is prime number
def prime(n):
    primeLst = []
    # 1 is prime number
    if n == 1:
        return True
    # if larger than 1, check if n can be divided by primes before n
    for i in range(2,n+1):
        found = False
        # build a prime num list
        for j in primeLst:
            if i % j == 0:
                found = True
                break
        # if number's met, not in list means it's prime 
        if i == n:
            if not found:
                return True 
            else:
                return False
        # only add when number can not be devide by current prime list
        else:
            if not found:
                primeLst.append(i)

# find the nth monisen number
# monisen number: if P is prime, M is prime and M = 2^P - 1. Call M monisen
def monisen(n):
    i = 1
    j = 0
    while True:
        i += 1
        if prime(i):
            yetM = 2**i-1
            if prime(yetM):
                j += 1
                if j == n:
                    return yetM

print(prime(15))

while True:
    n = int(input('enter a number:'))
    startTime = time.time()
    print(monisen(n))
    print(time.time()-startTime)