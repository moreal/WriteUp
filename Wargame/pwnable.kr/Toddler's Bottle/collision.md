# collision
can you use python?
little endian, big endian
## Overview
Daddy told me about cool MD5 hash collision today.
I wanna do something like that too!

ssh col@pwnable.kr -p2222 (pw:guest)

### Files
```
col  col.c  flag
```
### col.c
```c
#include <stdio.h>
#include <string.h>
unsigned long hashcode = 0x21DD09EC;
unsigned long check_password(const char* p){
        int* ip = (int*)p;
        int i;
        int res=0;
        for(i=0; i<5; i++){
                res += ip[i];
        }
        return res;
}

int main(int argc, char* argv[]){
        if(argc<2){
                printf("usage : %s [passcode]\n", argv[0]);
                return 0;
        }
        if(strlen(argv[1]) != 20){
                printf("passcode length should be 20 bytes\n");
                return 0;
        }

        if(hashcode == check_password( argv[1] )){
                system("/bin/cat flag");
                return 0;
        }
        else
                printf("wrong passcode.\n");
        return 0;
}
```

## Solution

문제의 코드를 보면 인자 하나, passcode를 받아서 20byte인지를 검사하고 그것을 check_password 함수에 넣어 그 반환값이 0x21DD09EC 인지를 묻고 있다.

check_password 함수는 char* 을 int*로 바꾸어 그 값들을 모두 더한 값을 반환한다.  

0x21DD09EC 을 5로 나눈 값을 python으로 해서 인자로 넣어주면 되겠다.

여기서 신경써야하는 것이 리틀에디언 빅에디언이다. 보통 리틀에디안이 많이 쓰이는 듯 하니 리틀에디언으로 도전해보자.

리틀 에디안은 갈수록 줄어든다. 무슨 말이냐면 우리가 "@#\$"라는 문자열을 입력하면 보통 메모리 주소 상에
@#\$ 같이 되어있는 걸을 생각한다.  
하지만 그건 빅에디안이고 리틀에디안은 갈수록 메모리 주소가 작아지므로 \$#@ 와 같이 저장이 된다.(설명이 이상했을 수도 있다,,)(그냥 역순)  

간단한 코드를 작성하여 나의 컴퓨터를 체크해 봤더니 인터넷에서 봤던 대로 리틀에디언이 맞는 것 같다.
```c
#include <stdio.h>

int main(int argc, char** argv) {
	int tmp = 0x12345678;
	char* a = (char*)&tmp;

	int i = 0;
	for (i = 0; i < 4; ++i)
		printf("%p %x\n",&a[i],a[i]);

	return 0;
}
```
```
000000000062FE3C 78
000000000062FE3D 56
000000000062FE3E 34
000000000062FE3F 12
```

주소 값이 점점 작아지는 것을 볼수 있다. (0x78이 가장 낮은 주소에 위치)

그렇다면 이 문제에는 어떻게 인자값을 넣어줘야 할까.

우리가 \x12\x34\x56\x78 로 값을 넣어주면 int 포인터로 읽을 때 0x78563412 로 읽을 것이다. 고로 우리는 \x78\x56\x34\x12 로 넣어 줘야지 0x12345678 로 인식 할 테니 실천에 옮겨보자.

0x21DD09EC = 568134124  
나누어 떨어지지 않는다.  
그러니 미리 14 정도 빼놓자  

568134110 / 5 = 113626822 = 6C5CEC6

6C5CEC6 4번과 저 값에 14(10)을 더한것을 한 번 더 더하면 되겠다
```python
"\x06\xC5\xCE\xC6" * 4 + "\x06\xC5\xCE\xD4"
```

이것을 리틀에디안 방식으로 바꿔주자.

```python
"\xC6\xCE\xC5\x06" * 4 + "\xD4\xCE\xC5\x06"
```

```python
./col `python -c 'print "\xC6\xCE\xC5\x06" * 4 + "\xD4\xCE\xC5\x06"'`
daddy! I just managed to create a hash collision :)
```

클리어~!!
