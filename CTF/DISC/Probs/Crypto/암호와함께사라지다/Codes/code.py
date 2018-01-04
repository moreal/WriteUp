#-*-coding:utf8-*-
#기본 원리
def isRelativeNumber(a,b):
    if (a>b): max=a
    else: max = b
    for i in range(2,max):
        if a % i == 0 and b % i == 0:
            return False
    return True
    
prime = raw_input().split(" ")
p = int(prime[0])
q = int(prime[1])
n = p*q

bn = (p-1)*(q-1)

e = 0

for i in range(2,bn):
    if isRelativeNumber(i, bn):
        e = i
        break

print "p:{} / q:{} / n:{} / bn:{} / e:{}".format(p,q,n,bn,e)

for d in range(1, 10000):
    if (e * d) % bn == 1:
        print "d is", d

"""
# 실전
#line = raw_input("Input n,e : ").split(" ") # It need d, 공개키 == (n, e)
n = 107 # int(line[0])
e = 493 # int(line[1])
values = raw_input("Input Values : ").split(",")
values = [int(i) for i in values]

# SH (N, E) (107, 493)
# e^value % n

for value in values:
    print chr(e^value % n)
"""