flag="H3X0R{H"
Crypto_message=[]
bit_encode=[]
bit_code= "abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789~!@#$%^&*()_+{}" #77word

result = [108, 255, 151, 167, 215, 173, 108, 33, 189, 189, 95, 118, 183, 0, 252, 118, 183, 170, 104, 118, 157, 255, 125, 49, 140, 118, 255, 134]
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
    answer_map = encode(flag + bit_code + '}')[7:]

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

173 ['Y', '{']
33 ['b', '@']
118 ['W', '_']
118 ['W', '_']
170 ['4', '(']
118 ['W', '_']
140 ['l', '+']
118 ['W', '_']
134 ['m', '}']
H3X0R{H@ppy_Ba9_B(g_L3ve+_3}

H3X0R{H@ppy_Ba9_B4g_L3vel_3}

"""