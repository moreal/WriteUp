# Cryingbag

## Overview

author : Dukup11ch1  
point : 350  
solvers : 15  

## Solution

해당 문제의 소스를 한번 봐보도록 하자

```python
a=[MOSAICED]    #private
b=[]                        #public
m=512                       #public
w=MOSAICED                     #private
n=(w-1)%m                   #private
flag="MOSAICED"
Crypto_message=[]
bit_encode=[]
bit_code="abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789~!@#$%^&*()_+{}"#77word
def make_cry():
    for i in a:
        b.append((i*w)%m)

def encode():
    for i in flag:
        bit_encode.append(bit_code.find(i))

    for i in range(0,len(bit_encode)):
        k=bit_encode[i]
        Crypto_message.append(0)
        for j in range(7):
            if k%2==1:
                Crypto_message[i]+=bit_encode[j]
            k=k//2

    print ("Encoded Message :",end=' ')
    print (Crypto_message)
    print ("b :",end=' ')
    print (b)
    print ("m :",end =' ')
    print (m)

if __name__ in '__main__':
    make_cry()
    encode()

```

뭔가 정말 길어서 처음에 딱보고서 이게 뭐지 하고 버렸던 문제다.

하지만 천천히 보다보면 쓸데 없는 변수들이 정말 많구나라는 것을 알 수있다 (인코딩 과정에서 쓰지 않는 변수들)

그래서 그 변수들을 없애고서 찬찬히 보다 보니 인코딩하는 문자열의 원문의 앞 7자리에 영향을 받는 다는 것을 알았다  

그래서 H3X0R{ 은 고정이 이니까 뒤의 한글자만 부르트 포스로 해서 구하고 그 값으로 해서 역연산 하여 구했다!!  

혹여나 중복되는 값들도 있었는데 게싱했다

## Flag
H3X0R{H@ppy_Ba9_B4g_L3vel_3}