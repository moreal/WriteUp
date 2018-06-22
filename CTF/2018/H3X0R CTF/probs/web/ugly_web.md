# ugly web

## Overview


## Solution
정말 간단하다

robots.txt를 보면 backup 파일을 받을 수 있는 곳이 있어서 해당 소스코드를 다운 받아 보기 시작했다

찬찬히 보다보면 extract($_REQUEST) 를 하는 것이 보인다 (아마..)

이것을 이욯해서 $_SESSION 의 변수 값들을 변조하면 admin으로 들어갈 수 있다

(맨 처음에는 SALT 값을 찾아야 하나 하고 찾고 있었다)