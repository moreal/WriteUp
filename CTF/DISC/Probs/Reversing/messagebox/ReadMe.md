# messagebox
840 point

## Overview
messagebox.exe를 실행해보니 "this wrong"이라는 메세지박스만 나오고 끝나버린다. 플래그를 찾기위해 올리디버그를 열고 분석해보자!  

HINT : FLAG에는 띄어쓰기가 있습니다.  
HINT 2 : XOR  

Download!

## Solution
(나는 Ollydbg 말고 x64dbg 라는 프로그램을 사용하였다., 설마 이게 문제가 될까)  

![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Reversing/messagebox/Image/StartMain.PNG)  

들어가서 메시지 박스가 뜨기전에 breakpoint를 걸어놓고 계속 진행시켰다.  

일단 "this wrong이라는 메시지 후 종료" 라는 이벤트(?)를 막기 위해 ZF 플래그 값을 수정하여  
해당 메시지가 뜨지 않게 하였다.  

![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Reversing/messagebox/Image/JumpSuccess.PNG)  

잘 넘어가는데 성공했다!!  
메시지박스에서 말하기를 "I'm Ayoung" 을 "I'm Han" 으로 바꾸라고 한다.  
그냥 메모리에 해당 문자열 값을 넣어줄때 그 주소를 살짝 바꿔주었다.  

![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Reversing/messagebox/Image/EditASM.PNG)  

그랬더니 잘 통과해서 콘솔에 문자열을 출력하기 시작했다!  

![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Reversing/messagebox/Image/ShowFLAG1.PNG)  
![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Reversing/messagebox/Image/ShowFLAG2.PNG)   
![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Reversing/messagebox/Image/ShowFLAG3.PNG)  

그리고서는 프로그램이 종료 되었다.
콘솔에 떴던 메시지는 다음과 같다.

```
# 약간 줄바꿈을 했다.  
0x40, 0x4d, 0x57, 0x47, 0x7f, 0x35,  
0x24, 0x6c, 0x44, 0x72, 0x61, 0x24,  
0x65, 0x24, 0x67, 0x6c, 0x34, 0x67,  
0x6b, 0x68, 0x44, 0x70, 0x37, 0x79  
you can use number '4' to decode flag
```

이 hex 값들을 4를 이용해서 바꾸라는 의미인가보다!!  
이 값들을 xor 4 연산을 하면은 Flag가 나올 것 같다!!

```python
# 원래는 콘솔에다가 했었지만 코드를 정리해 놓는다.
print "".join([chr(int(i,16) ^ 4) for i in raw_input("Input data : ").replace("0x","").split(",")])
```

그 결과는 다음과 같다.

```console
>>> print "".join([chr(int(i,16) ^ 4) for i in raw_input("Input line : ").replace("0x","").split(",")])
Input line : 0x40, 0x4d, 0x57, 0x47, 0x7f, 0x35, 0x24, 0x6c, 0x44, 0x72, 0x61, 0x24, 0x65, 0x24, 0x67, 0x6c, 0x34, 0x67, 0x6b, 0x68, 0x44, 0x70, 0x37, 0x79
DISC{1 h@ve a ch0col@t3}
```

## Flag
DISC{1 h@ve a ch0col@t3}
