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
