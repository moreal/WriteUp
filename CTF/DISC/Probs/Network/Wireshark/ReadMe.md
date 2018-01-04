# Wireshark
600 point

## Overview
와이어샤크..? 그게 뭐지??  

Download!  

## Solution
문제에서 주는 파일을 다운 받아서 Wireshark 로 열었더니  
누군지는 몰라도 누군가의 사용에 의한 패킷들이 나열되어 있었다.  

![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Network/Wireshark/Image/Hello.PNG)  

눈에 띄는 것은 어떤 한 이미지 파일에 대한 HTTP Request 였다. 일단 Host가 lapio.kr 이라는 것 부터가 문제 출제자가 넣었으리라 생각했다.  
그래서 그 주소로 들어가 봤더니 없습니다!! 라고 떴다.  

![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Network/Wireshark/Image/NotFound.PNG)  

이 패킷캡처 파일에서 패킷은 Response 도 담고 있었다.  
그리고 그곳에는 이미지 바이너리가 담겨있었고 export 하여 사진을 열었더니  

![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Network/Wireshark/Image/Response.PNG)  
![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Network/Wireshark/Image/Export.PNG)  

누가 그렸는지는 몰라도 정말 개성 넘치고 보기 좋은 잘 그린 그림이 있었다.(Good)  

![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Network/Wireshark/Flag.png)  

그리고 같이 나와있는 플래그를 Auth 해서 클리어 하였다.  

// 혼자 생각하건데 hitomi 는 대체 어떻게 찾은 걸까 (물론 건전한 블로그, 이걸 들어가야 하나 고민했었다,,)  

## Flag
DISC{H3lp_m3@@!!}
