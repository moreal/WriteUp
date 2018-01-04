#-*-coding:utf8-*-

d = int(raw_input("Input d :"))
n = int(raw_input("Input n :"))
string = raw_input("Input String :").split(",")
string = [int(c) for c in string]

result = ""
for c in string:
    result += chr( c ** d % n )
    
print result