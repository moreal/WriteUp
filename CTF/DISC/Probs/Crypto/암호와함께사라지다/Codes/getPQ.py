#-*-coding:utf8-*-
def isPrimeNum(n):
    for i in range(1,n):
        if n % i == 0:
            return False
    else: return True

n = int(input())

for p in range(1, n+1):
    if n % p != 0: continue
    print p, n/p
    if isPrimeNum(p) and isPrimeNum(n / p):
        print "P",p,"Q", n/p
        break