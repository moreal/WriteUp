# sp0ng3b0b
760 point

## Overview
스폰지밥이다!!!

HINT : LFI
HINT 2 : 'base64' 라는 문자열을 필터링 하고있습니다.

바로가기

## Solution

![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Web/sp0ng3b0b/Image/main.png)  

폼 이외에는 아무 것도 없다.  

![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Web/sp0ng3b0b/Image/sponge.png)  

들어가게 되면 다음과 같이 그냥 이미지를 띄워준다.  

근데 힌트를 보아하니 LFI(Local File Inclusion) 라고 하길래  
혹여나 하는 마음에 form 버튼의 내용은 hello로 바꿔 보았다. 그랬더니 그렇다고 한다.  

![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Web/sp0ng3b0b/Image/itisLFI.png)  

다음 에러 출력문에서 우리가 알 수 있는 것은 다음과 같다.
- post로 보낸 character의 값에 ".php" 를 더한 그것을 include_once를 통해서 호출한다.
- 확장자 까지 입력해줄 필요가 없다.  

그래서 직접 flag.php로 들어가 봤으나 아무 것도 없었지만 Not Found 에러는 나지 않았기에 있다는 것을 확인할 수 있었다.  

아마도 php내에서 처리만 하고 출력은 없는 듯하니 php의 소스를 직접 읽어야 했다.  

그래서 php://filter 스트림을 사용하기로 했다.

그래서 다음과 같이 button의 내용을 바꾸어 flag.php의 내용을 가져왔다.  

> php://filter/convert.quoted-printable-encode/resource=flag
> php://filter/string.rot13/resource=flag

그리고 그 값을 decode 하여 flag를 찾았다.  

### flag.php
```php
<?php
  $flag = "DISC{b0gl3_b0gl3_sp0ng3b0b_h4h4h4h4h4h4_XD}";
?>
```
### spongebob.php
그냥 궁금해서 해봤다.
```php
<?php
  echo "<img src=\"https://cdn.vox-cdn.com/thumbor/0jbIJZPcxu4WmYZZZQW3KNLiXns=/0x0:1024x576/1200x800/filters:focal(431x207:593x369)/cdn.vox-cdn.com/uploads/chorus_image/image/54925925/spongebob_rainbow_meme_video_16x9.0.jpg\"
?>
```
## Flag
DISC{b0gl3_b0gl3_sp0ng3b0b_h4h4h4h4h4h4_XD}
