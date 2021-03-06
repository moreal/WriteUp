# Mixed_breed
200 point

## Overview
String Replace는 쉽게 말해 문자열의 형태를 바꿔주는 것이다.
str_replace("king","queen","theking"); 을 예시로 들면 theking이라는 문자열에서
king을 queen으로 바꿔주라는 말이다.

Decoding 즉 복호화는 암호화된 정보를 암호화되기 전으로 돌리는 처리 혹은 그 방법을 말한다.
base64 암호화 방식은 그 끝이 =으로 끝나서 알아보기 쉽다.

해시암호란 평문 즉 어떠한 문장을 해시알고리즘을 통해 해시값으로 출력하는 것을 말한다.
띄어쓰기 등의 약간의 변화에도 해시값은 완전 다른 값이 나오기 때문에,
해시값은 주로 데이터의 위,변조여부를 확인하는데 사용된다.

해시함수의 종류는 MD5, SHA-1, SHA 224 등이 있다.
아 참고로 Mixed breed는 혼종이라는 말이다.

HINT : 복호화  

## Solution
![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Web/Mixed_breed/Image/Firstpage.PNG)  
처음에 들어가면 패스워드와 패스코드를 입력하는 폼이 기다리고 있었다.

그리고 소스코드를 보면 다음과 같은 코드가 나와있다.

```html
<!DOCTYPE html>
<head>
  <title>Web_Prob!!!!</title>
</head>
<body>
</body>

<!DOCTYPE html>
<head>
  <title>Web_Prob!</title>
</head>
<body>
  <!-- VEdrNWNHSnRVbXhsUXpWM1lVaEJMMk15T1RGamJVNXNXVEk1YTFwUlBUMD0= -->
  <form method="get" action="./index.php">
    Input Password : <input type="text" name="password"><br/>
    Input Passcode : <input type="text" name="passcode">
   <input type="submit" value="Check">
  </form>
</body>
```
<br>
어떤 한 주석이 눈에 띈다.  
```html
<!-- VEdrNWNHSnRVbXhsUXpWM1lVaEJMMk15T1RGamJVNXNXVEk1YTFwUlBUMD0= -->
```

끝에 보면 =를 사용하는 걸 보니 base64 방식인가 보다.  
풀어주면(2번으로 안되서 3번 했더니 나온다) ./index.php?sourcecode 가 나온다.

그래서 해당 url로 들어가 소스코드를 살펴 보았다.

```php
<?php
include ("./hint.php");

  if(isset($_GET["sourcecode"])){
    highlight_file(__FILE__);
  }

$password = "lapio best";

if(isset($_GET["password"])){

  if(preg_match('/\s/',$_GET["password"])){
    $input_password=str_replace("best","",$_GET["password"]);
  }else{
    $input_password=$_GET["password"];
  }

  if($input_password == $password){
      $Input_passcode = $_GET["passcode"];

      if($Input_passcode>7 || $Input_passcode<0){
        $Input_passcode = 1;
        }

      if($Input_passcode>4 && $Input_passcode<5){
        echo "Hint is...215ahs";
        echo "=> $hint";
        }else{
        echo "passcode is fail....";
          }
      }else{
            die("password is fail..");
          }
  }

?>

<!DOCTYPE html>
<head>
  <title>Web_Prob!</title>
</head>
<body>
  <!-- VEdrNWNHSnRVbXhsUXpWM1lVaEJMMk15T1RGamJVNXNXVEk1YTFwUlBUMD0= -->
  <form method="get" action="./index.php">
    Input Password : <input type="text" name="password"><br/>
    Input Passcode : <input type="text" name="passcode">
   <input type="submit" value="Check">
  </form>
</body>
```

대충 요약하자면 password 파라미터는 best를 str_replace로 없애버리고  
만약 필터링된 password가 $password, "lapio best"와 같다면 passcode 파라미터를 검사한다.  
<br>
만약 7 초과 0 미만이라면 1로 값을 수정하고  
passcode 가 4보다는 크고 5보다는 작을 경우 hint를 출력해준다.  
<br>
그래서 이것들을 우회하기 위해서 다음과 같은 값을 입력해 주었다.  

> password : lapio besbestt  
> passcode : 4.5  

결과는 다음과 같다.

![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Web/Mixed_breed/Image/FirstStageInput.PNG)  
![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Web/Mixed_breed/Image/FirstStageClear.PNG)

성공!! Hint 값이 출력되었다.

해당 값은 215ahs.. sha512 라고 직접적이지 않은 직접적인 힌트를 주고 있다.

자 그러면 이것도 다시 디코딩 해주자.

![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Web/Mixed_breed/Image/SecondStageClear.PNG)

결과 적으로 **7e432d6f6cc2100e03523d8985c914f3ca3f522af7799564d48c37af231c9d5b9acbc45201e139cdab4a01c7aadb4f8e4f9a2990eb3ef699f6495055cedea0d4** 가 ./hint.php?readme 를 의미함을 알 수 있었다.  
그러면 문제의 의도대로 들어가주자.  

![Image](https://github.com/moreal/WriteUp/blob/master/CTF/DISC/Probs/Web/Mixed_breed/Image/LastClear!!.PNG)

우리를 기다리고 있는 Flag 가 있었다. **클리어!!** (혼종..)

## Flag
DISC{WH2_5O_S2RIOU5}
