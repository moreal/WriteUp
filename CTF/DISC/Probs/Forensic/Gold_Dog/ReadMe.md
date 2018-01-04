# Gold_Dog
360 point

## Overview
2018년의 띠는 황금개띠다.  
이를 기념하여 동아리 Lapio의 부장 K 군은 동아리원 S 양에게 황금개 그림을 그려달라고 외주를 맡겼다.  
3일간 공을 들여 그리기 작업을 마친 S 양은 K 군에게 그림을 제출하려고 하였으나 의문의 괴한 J 군에게 암살당하였고,  
괴한 J 군은 자신의 흔적을 남기는 사이코패스여서, 해당 그림에 자신의 메시지를 남겨두었다.
수사관인 당신은 J 군의 메시지를 찾아야한다.  

J 군의 메시지로 확인되는 것을 찾은 후, 해당 메시지를 DISC{메시지} 형식으로 플래그에 등록하라.  

HINT : 메모장으로 열어도 나올 것 같은데..?  

## Solution
![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Forensic/Gold_Dog/Image/Forensic100_Gold_Dog.png)  

해당 그림이다.  

이 것을 메모장으로 열어보면 아래쯤에 플래그로 보이는 것이 있다.  
(맨 처음에는 이것이 height을 늘리는 문제인 줄 알고서 한 10분 정도 소요 했던 것 같다)  

![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Forensic/Gold_Dog/Image/Flag.PNG)  

DISC{} 형식으로 만들어 Auth 하면 클리어!!

## Flag
DISC{PNG_FI13_F0rmat!!}
