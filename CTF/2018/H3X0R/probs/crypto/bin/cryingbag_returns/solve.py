flag="H3X0R{"
Crypto_message=[]
bit_encode=[]
bit_code= "abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789~!@#$%^&*()_+{}" #77word

result = [108, 255, 151, 167, 215, 184, 176, 49, 180, 129, 156, 101, 129, 131, 137, 49, 129, 33, 49, 0, 55, 137, 145]
answer = ""

def encode(flag):
    Crypto_message = []
    bit_encode = []
    for i in flag:
        bit_encode.append(bit_code.find(i))
        # print(bit_encode)

    for i in range(0,len(bit_encode)):
        k = bit_encode[i]
        Crypto_message.append(0)
        for j in range(7):
            # print(f"[i] k is {k} , j is {j} => {Crypto_message[i]}")
            if k%2==1:
                Crypto_message[i]+=bit_encode[j]
            k=k//2

    # print ("Encoded Message :",)
    return Crypto_message

# 앞의 7 자리 비트 수 만큼 bit_encode를 더한다
def decode(enc):
    pass

def rindex(mylist, myvalue):
    return len(mylist) - mylist[::-1].index(myvalue) - 1

if __name__ in '__main__':
    # for c in bit_code:
        # print(flag + c + '}')
        # print(encode(flag + c + '}'))
        # print(encode(flag + c + '}'))
        # print(encode(flag + c + 'ddd}'))
        
    print(encode(flag + bit_code))
    print(result)

    for c in bit_code:
        if encode(flag + c + '}')[5] == result[5]:
            answer_map = encode(flag + c + bit_code + '}')[7:]
            break

    dic = {}

    for a, b in zip(answer_map, bit_code):
        # print(type(a), type(b))
        if a in dic:
            dic[a] += [b,]
        else:
            dic[a] = [b,]

    for el in result:
        # print(dic[el])
        if len(dic[el]) != 1:
            print(el, dic[el])
            answer += dic[el][1]
        else:
            answer += dic[el][0]

    print(answer)

    
"""
My Guess Time..

151 ['X', '+']
H3+0R{Sex_on_the_beach}

H3X0R{Sex_on_the_beach}

"""