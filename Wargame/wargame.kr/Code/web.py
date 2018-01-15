#-*- coding:utf8 -*-

import urllib2, urllib, sys

WEB_PHPSESSID = 'kvkemdvcf9bqkcmk5v2c51chk4'
WEB_USER_AGENT = 'Mozilla/4.0'

def getRequest(url, inject_url="", show=True):
    if inject_url is not "": url = url.format(urllib.quote(inject_url))
    if show: print url
    req = urllib2.Request(url)
    req.add_header('User-Agent', WEB_USER_AGENT)
    req.add_header("Cookie","PHPSESSID=" + WEB_PHPSESSID)
    return req

def getPage(req):
    return urllib2.urlopen(req).read()

def setPHPSESSID(id):
    WEB_PHPSESSID = id

def setUSERAGENT(agent):
    WEB_USER_AGENT = agent

def toUnicode(data, f="", file_write=False):
    result = ""
    for i in data:
        result+=unichr(i)

    if not file_write:
        return result.encode("utf-8")
    else:
        f = open(f, "w")
        f.write(result.encode("utf-8"))

def toFile(path, data):
    f = open(path, "w")
    f.write(data)
    f.close()
