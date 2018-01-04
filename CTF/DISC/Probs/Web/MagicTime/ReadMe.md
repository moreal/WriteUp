# MagicTime
200 point

## Overview
매직 해쉬란 php가 ==연산을 할 때, 서로 다른 값이 같은 값으로 인식되도록 하는 특수한 동작을 말한다.  
이 특수한 동작이 일어나기 위해서는 조건이 있는데, 바로 문자열을 0e로 시작해야한다는 것이다.  
이를 방지하기 위해 md5와 sha1 등으로 암호화를 했는데,  
암호화를 통한 결과가 0e로 시작되는 경우가 있다고 한다. 그 경우를 찾아 보자!!!  

## Solution
![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Web/MagicTime/Image/EmptyPage.PNG)

텅텅빈 페이지가 우리를 기다리고 있다.  

```html
<!DOCTYPE html>
<head>
  <title>Prob!</title>
</head>
<body>
  <!-- ./index.php?view-source -->
  <form method="get" action="./index.php">
    <input type="text" name="key2">
    <input type="submit" value="확인">
  </form>
</body>
```
소스코드를 봤더니 소스를 볼수 있는 파라미터를 알려준다.  
들어가 보자.  

```php
<?php
  include("./flag.php");
  $_key1=md5("aabg7XSs");
  if(isset($_GET['key2'])){
    if($_GET['key2']=="aabg7XSs"){
      echo "Not this answer";
    }elseif($_key1==md5($_GET['key2'])){
      echo "Congratulation!!! Flag is.... $flag";
    }else{
      echo "fail";
    }
  }
  if(isset($_GET["view-source"])){
    show_source(__FILE__);
  }
 ?>

<!DOCTYPE html>
<head>
  <title>Prob!</title>
</head>
<body>
  <!-- ./index.php?view-source -->
  <form method="get" action="./index.php">
    <input type="text" name="key2">
    <input type="submit" value="확인">
  </form>
</body>
```  
<br>
요약하자면 aabg7XSs 를 md5 암호화 한것과 내가 입력한 것의 md5 암호화 값이 서로 같아야 한다.  
<br>
aabg7XSs 를 md5encryption.com에서 돌려보니 0e087386482136013740957780965295 라는 값이 나왔다.  
이 값을 float 방식으로 표현하면 0의 087386... 승인 것이다. 0은 아무리 곱해도 0이니 결국엔 0이다.  

이렇게 의도치 않은 일이 일어나는 경우가 있고 그렇게 만드는 경우가 이런 경우다.  
이런 값을 매직해시 라고 불렀던 것 같다. 어찌됬든 그러면 우리도 md5를 해서 0e로 시작하는 값을 입력해 주면 되겠다! 일단 aabg7XSs는 필터링 해놓았으니 다른 값을 찾아보자.  

구글에 검색해보면 그런 값이 몇 나온다.  
나는 그 중 240610708를 입력했다.

![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Web/MagicTime/Image/InputMagicHash.PNG)  
![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Web/MagicTime/Image/Clear.PNG)

**클리어!!**

## flag
DISC{THIF_IF_NET_FLAG}
