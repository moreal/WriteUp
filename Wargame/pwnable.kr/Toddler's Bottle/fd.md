# fd
File Descriptor

##Overview
Mommy! what is a file descriptor in Linux?

* try to play the wargame your self but if you are ABSOLUTE beginner, follow this tutorial link: https://www.youtube.com/watch?v=blAxTfcW9VU

ssh fd@pwnable.kr -p2222 (pw:guest)

### Files
```console
fd  fd.c  flag
```

### fd.c

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char buf[32];

int main(int argc, char* argv[], char* envp[]){
        if(argc<2){
                printf("pass argv[1] a number\n");
                return 0;
        }
        int fd = atoi( argv[1] ) - 0x1234;
        int len = 0;
        len = read(fd, buf, 32);
        if(!strcmp("LETMEWIN\n", buf)){
                printf("good job :)\n");
                system("/bin/cat flag");
                exit(0);
        }
        printf("learn about Linux file IO\n");
        return 0;

}
```

## Solution
리눅스는 파일 stream을 열면서 fd를 제공한다.  
그리고 명시적으로 프로그램당 스트림을 열어 놓는데 0,1,2는 stdin,stdout,stderr 의 fd이다.  

그러므로 코드에서 볼 때 argv[1] 의 값을 정수형으로 변환하여 0x1234를 뺀 값을 fd로 삼고 그 fd에서 32바이트 만큼 읽어오고 그 읽어온 값이 LETMEWIN이면 클리어 한다!  

0x1234 는 십진수 4660 과 같다.

그러므로 첫번째 인자의 4660을 입력해주고 프로그램내에서의 입력에서 LETMEWIN을 입력해주면 클리어 한다.  

```
./fd 4660
LETMEWIN
```

그러자 flag 메시지가 뜬다!

## 기본적인 상식
파일을 실행할 때 main함수는 다음과 같은 인자들을 받을 수 있다.
```c
int argc, char* argv[], char* envp[]
```
argc는 arg(인자)의 count(갯수) 값을 가진다.  
argv는 인자 문자열들을 받는다.  
envp는 환경변수에 대한 포인터이다.

> 여기서 문제, 왜 argc < 2 라고 문제 코드에서 말했을 까?

기본적으로 첫번째 인자는 해당 프로그램의 절대경로 문자열을 가진다.
그렇기에 argc의 최솟값은 1인것이다.
