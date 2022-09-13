# block I/O vs non-block I/O

## Intro : I/O란?

> input/output 데이터의 입출력

I/O의 종류 : **networt(socket)**, file, pipe(프로세스간 개념), device(모니터, 키보드)

### Socket

네트워크 통신은 socket을 통해 데이터가 입출력이 됨

소켓(Socket)이란 네트워크상에서 동작하는 **프로그램 간 통신의 종착점(Endpoint)** <br>
관련 내용을 정리한 적이 있으니 다시 [리마인드](https://github.com/fhwmqkfl/YJs_TIL/blob/main/CS/네트워크/socket.md)!

## **1. block I/O**

I/O작업을 요청한 프로세스/스레드는 요청이 완료될 때까지 블락됨<br>
_cpu의 기본적인 I/O 모델_ 로 리눅스에서 모든 소켓 통신은 기본 blocking으로 동작한다.

<img width="707" alt="스크린샷 2022-09-13 오후 2 05 58" src="https://user-images.githubusercontent.com/71719160/189813675-c8df6d9d-a6f0-41e0-880e-4ba9ad1a0dda.png">

1. read system call 읽는 순간 thread는 사용할 수 없게 블락되고, 커널모드로 전환됨
2. 커널에서 read I/O를 읽고 해당 입출력 진행
3. 시간이 지나 (kernel)read response이 되면 응답을 받고 data를 커널 스페이스에서 유저스페이스로 옮김 (이때 블락이 없어지고 준비된 데이터를 읽고 스레드가 실행)

## **2. non-block I/O**

프로세스/스레드를 블락시키지 않고 요청에 대한 현재 상태를 바로 리턴함

<img width="707" alt="스크린샷 2022-09-13 오후 2 06 24" src="https://user-images.githubusercontent.com/71719160/189813729-ef8bc5d4-afe3-40ab-9241-29d7c6e627a0.png">

1. read system call 읽는 순간 커널모드로 전환되고 read I/O실행됨
2. (리턴값이 준비되지 않았음에도)바로 readI/O에서 (리눅스기준)-1 & ‘EAGAIN/EWOULDBLOCK’라는 에러 코드 리턴
3. 스레드는 다른 값을 처리할 수 있게 됨
4. 도중에 응답값이 준비됨
5. 스레드는 계속 진행하다가 다시 non-blocking system call을 하는데 이때 커널로 전환되면서 응답값을 가지고 유저 스페이스로 데이터 보냄

### non-block I/O이슈 ⇒ I/O 작업 완료를 어떻게 확인할 것인가?

1. 완료됬는지 반복적으로 확인
  * 수시로 원하는 데이터가 준비되었는지 non-blocking system call을 통해 물어본다 <br> → 완료된 시간과 완료를 확인한 시간의 갭이 있어 처리속도 느려질 수 있음 + cpu낭비 발생
    
2. I/O multiplexing(다중입출력)사용 ⇒ 네트워크 통신에 많이 사용
  
  * 다중입출력 : 관심있는 I/O 작업들을 동시에 모니터링 하고 그중에 완료된 I/O작업을 한번에 알려줌
  
    <img width="678" alt="스크린샷 2022-09-13 오후 2 18 23" src="https://user-images.githubusercontent.com/71719160/189815190-d5ce4e08-bc61-4cab-9fb7-c6d6047ad9c7.png">

    1. I/O multiplexing 시스템 콜을 통해 2개의 소켓을 논블러킹으로 리드하게 함
    2. (1번의 작업에서 어떻게 시스템콜을 호출하느냐에 따라 스레드는 blocked/run달라짐) ⇒ 여기서는 스레드 블락된다고 가정
    3. 동시에 2개의 소켓에 모두 데이터가 들어옴 (response받음)
    4. notify data avaliable라는 알람을 받음
    5. 첫번째, 두번째 소켓을 순서대로 받아 처리
    
    종류: select, poll, epoll(리눅스), kqueue(맥), IOCP(I/O completion port)(윈도우)가 많이 쓰임
    
3. callback/signal 사용(posix aio, linux aio)
    
    <img width="675" alt="스크린샷 2022-09-13 오후 2 24 57" src="https://user-images.githubusercontent.com/71719160/189816009-f5795b68-30b0-4640-949c-853ef09b840a.png">
    1. aio_read로 시스템 콜 호출 -> 커널은 readI/O동작
    2. 1번과 별개로 스레드는 독립적으로 동작
    3. 디바이스로 부터 read response가 오면 이때 데이터가 처리가 되는데, callback/signal로 처리가 된다



    
