# MY_FLAG
680 point

## Overview
파일 전송 프로토콜 FTP(File Transfer Protocol)는 인터넷상의 컴퓨터들간에 파일을 교환하기 위한 표준 인터넷 규약이다.  
파일 시그니처(File Signatures)는 파일 포맷별로 존재하는 고유한 시그니처이다. 파일의 맨 앞에 존재하는 시그니처는 헤더 시그니처라 하고, 맨 끝에 존재하는 시그니처를 푸터 시그니처라 한다.  

HINT : Statistics ->Protocol Hierarchy를 이용하면 패킷에 어떤 프로토콜들이 있는지 쉽게 확인할 수 있다.  

Download!

## Solution

해당 패킷캡처 파일을 와이어샤크로 열어보았다.  
열어 보았더니 다음과 같이 FTP 패킷들이 눈에 들어온다  

![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Network/MY_FLAG/Image/Packets.PNG)  

그렇게 살펴 보던 도중 파일을 전송하는 것을 볼 수 있었다. (파일명 : Sea.zip)

![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Network/MY_FLAG/Image/FileTransfer.PNG)  

그래서 ftp 필터링을 풀고 전체를 봤더니 파일을 전송하고 있는 패킷들이 보인다.

![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Network/MY_FLAG/Image/doing.PNG)  

그래서 해당 데이터 들을 byte로 export해서 그것들을 모두 합쳐서 압축을 해제했다.
그랬더니 안에 Octo 와 pus 파일이 있었고 Octo를 열었을 때 PNG의 헤더가 있었다.  

그래서 둘을 Octopus.png 로 합쳐 사진을 열었다.  
안녕 플래그!!  

![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Network/MY_FLAG/Octopus.png)  

// 문제에서 말했듯이 파일 헤더에 문제가 있었는데 Zip 파일의 Extra field Length 값이 손상되었던 듯 한데 알집에서 복구기능으로 복구해 줬다.  

## Flag
DISC{Oct@ps4}
