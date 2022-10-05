# Cross-Origin Resource Sharing(CORS)정책

## CORS의 정의

CORS은 `Cross-Origin Resource Sharing`의 약자로 W3C에서 내놓은 정책이다. <br>
특정 헤더를 통해서 브라우저에게 한 출처(origin)에서 실행되고 있는 웹 애플리케이션이 다른 출처(cross-origin)에 원하는 리소스에 접근할 수 있는 권한이 있는지 없는지를 알려주는 매커니즘이다.

    주의 ! 출처가 다른 두개의 리소스가 마음대로 소통되는 환경이라면 XSS, CSRF등의 방법으로 보안적 이슈가 발생할 가능성이 매우 높다!!!

### 출처(Origin)
특정 페이지에 접근할 때 사용되는 URL Scheme(프로토콜), host(도메인), 포트를 의미
same-origin : 프로토콜,도메인, 포트가 같음
cross-origin : 위 세가지중 하나라도 다른경우!

💡 `https://github.com/fhwmqkfl:80`를 기준으로 가정

| url                                 | 같은 출처 | 이유                             |
|-------------------------------------|-------|--------------------------------|
| https://github.com/fhwmqkfl/YJs_TIL | 　O    | Scheme(프로토콜), host(도메인), 포트 동일 |
| https://test@github.com/fhwmqkfl    | O     | Scheme(프로토콜), host(도메인), 포트 동일 |
| http://github.com/fhwmqkfl:80       | X     | Scheme(프로토콜)이 다르다              |
| https://github.com/fhwmqkfl:8000    | ?     | 브라우저에 따라 다르게 적용될 수 있음          |


> 다른 출처로 오는 리소스 요청을 제안하는 방법
> 1. CORS
> 2. SOP(Same-Origin Policy) : 같은 출처에서만 리소스를 공유할 수 있다는 규칙을 가진 정책


## CORS의 동작방법

> 서로 다른 출처를 가진 리소스를 안전하게 사용할수 있는 방법

기본적으로 웹 클라이언트 어플리케이션이 다른 출처의 리소스를 요청할 때는 HTTP 프로토콜을 사용하여 요청을 보내게 되는데, <br>
이때 브라우저는 요청 헤더에 `Origin`이라는 필드에 요청을 보내는 출처를 함께 담아보낸다.

```markup
Origin: https://github.com/fhwmqkfl
```

이후 서버가 이 요청에 대한 응답을 할 때 응답 헤더의 `Access-Control-Allow-Origin`이라는 값에 “이 리소스를 접근하는 것이 허용된 출처”를 내려주고,<br>
이후 응답을 받은 브라우저는 자신이 보냈던 요청의 `Origin`과 서버가 보내준 응답의 `Access-Control-Allow-Origin`을 비교해본 후<br>
이 응답이 유효한 응답인지 아닌지를 결정한다.

CORS의 동작은 총 3가지의 시나리오에 따라 변경된다.
### 시나리오 1. Preflight Request
일반적으로 자주 보는 케이스.<br>
해당 시나리오에서 브라우저는 요청을 예비/본 요청으로 나누어 서버에 전송한다<br>
예비 요청에서 HTTP메소드중 OPTION 메소드가 사용되며, 예비요청을 통해 브라우저가 요청을 보내는게 안전한지 한번 체크한다.

### 시나리오 2. Simple Request
시나리오 1과 다르게 예비요청을 보내지 않고 바로 본 요청을 보낸다.<br>
서버가 응답할 때 `Access-Control-Allow-Origin`을 보내고 그때 브라우저가 CORS정책 위반 여부를 검사한다.

예비 요청을 생략하는데 특정 조건을 만족하는 경우에만 예비 요청을 생락햘 있다
> 조건 1. HTTP 메소드는 POST, GET, HEAD중 하나<br>
> 조건 2. Accept, Accept-Language, Content-Language, Content-Type, DPR, Downlink, Save-Data, Viewport-Width, Width를 제외한<br> 헤더를 사용하면 안된다.<br>
> 조건 3. 만약 Content-Type를 사용하는 경우에는 application/x-www-form-urlencoded, multipart/form-data, text/plain만 허용된다.

### 시나리오 3. Credentialed Request
인증된 요청을 사용하는 방법으로 시나리오 1,2보다 좀더 보안을 강화할때 사용한다.<br>
`credentials` 옵션을 이용해 요청시 인증과 관련된 정보를 담을 수 있게 하는 방식을 사용한다
credentials의 종류는 아래 3가지가 있다
* same-origin(기본값) : 같은 출처간 요청에만 인증정보를 담을 수 있다
* include : 모든 요청에 인증정보를 담을 수 있다
* omit : 모든 요청에 인증정보를 담지 않는다
