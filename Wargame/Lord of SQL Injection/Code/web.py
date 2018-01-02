#-*- coding:utf8 -*-

import urllib2, urllib

def getLength(url, success, arr=list(range(1,99))):
    for i in arr:
        new_url = url.format(i)
        if success in urllib2.urlopen(urllib2.Request(new_url)).read(): return i
    return -1
    
def bruteForce(url, success, 