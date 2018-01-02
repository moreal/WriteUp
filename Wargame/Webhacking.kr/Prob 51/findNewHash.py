import hashlib

for TEST in range(0,999999999):
    if "'='" in hashlib.md5(str(TEST)).digest(): print "HELLO", str(TEST)