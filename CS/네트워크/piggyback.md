# 피기백(Piggyback)방식

> 수신측에서 수신된 데이터에 대한 확인을 즉시 보내지 않고<br>
> 전송할 데이터가 있는 경우, 제어프레임 사용 없이 `기존의 데이터 프레임에 확인필드를 덧붙여 전송하는 흐름제어 방식`

네트워크 대역폭을 효율적으로 사용하기위한 기술

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FTJbGA%2Fbtrs2EbBSRH%2FZVN8YoLQfKJAzplmtDAEDK%2Fimg.png">

만일 데이터 덧붙이지 않고 ACK로 응답후 메세지에 대한 응답을 보낸다면 2번의 전송이 일어남<br>
이때 한번에 ACK와 메세지에 대한 응답을 같이 보낸다면 전송은 1번만 일어나게 된다

* 장점 : 네트워크 대역폭을 효율적으로 관리할 수 있다
* 단점 : ACK를 보내기 까지 오랜시간이 걸릴경우 송신쪽 타임아웃에 의한 재전송이 일어날 수 있다