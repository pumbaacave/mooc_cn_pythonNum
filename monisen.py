# define if number is prime number
def prime(n):
    if n == 1:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

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

print(monisen(4))