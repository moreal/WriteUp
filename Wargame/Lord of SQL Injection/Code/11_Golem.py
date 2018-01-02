#-*- coding: utf-8 -*-
import urllib2, urllib


# payload = '||'
url = "http://los.eagle-jump.org/golem_39f3348098ccda1e71a4650f40caa037.php?pw={}"

req = urllib2.Request(url.format(""))
req.add_header('User-Agent','Mozilla/4.0')
req.add_header("Cookie","PHPSESSID=vo43bc6uk9dnvbalb1jfvf7pp4")

page = urllib2.urlopen(req)
print page.read()
