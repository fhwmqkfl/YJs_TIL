# 동기와 비동기 / 동시성과 병렬성

## 동기(synchronous) & 비동기(asychronous)
어떤 작업을 처리하는 과정에 대한 차이에 따라 나뉜다.

### 동기(Sync)
하나의 작업에 대한 요청에 동시에 응답이 오는것<br>
main은 block된 상태이므로 작업이 끝날때까지 다른 작업을 할 수 없다 -> 대기시간이 길어진다면 자원이 낭비될수 있음

-> 동기가 필요한 경우는 특정작업의 영향이 다음 작업에 영향을 미칠때임
### 비동기(Async)
요청에 대한 응답이 동시에 일어나지 않음<br>
대기시간을 낭비하지 않고 다른 일을 처리할수 있다

> 동기&비동기에서 관련되는 개념이 Blocking과 Non-Blocking!
> 
> [blocking/non-blocking관련 git정리내용](https://github.com/fhwmqkfl/YJs_TIL/blob/main/CS/blockIO_nonblockIO.md)<br>
> 일반적으로 동기 = Blocking, 비동기 = Non-Blocking이라고 생각하지만 완전히 동일한게 아님<br>
> Synchronous는 작업완료의 여부를 따지고,  Blocking은 쓰레드의 입장에서의 제어권관련이니 관심사가 서로 다름!<br>
> 그래서 Synchronous이면서 Non-blocking도 있을 수 있고, 반대로 Asynchronous이면서 Blocking 조합도 있을수 있다!<br>

## 동시성(Concurrency) & 병렬성(Parallelism)
<img src="https://t1.daumcdn.net/cfile/tistory/99AD02405FBBB94910">

### 동시성 
<img src="https://velog.velcdn.com/images%2Fcha-suyeon%2Fpost%2Fe13b6da0-c211-44d6-a8bf-a7dee3d539b3%2Fimage.png">
싱글코어 환경에서 단일 프로세스내에 멀티스레드를 동작해 구현하는 것으로<br>
여러 작업이 동시에 실행되는것처럼 구현되는것


### 병렬성
<img src="https://velog.velcdn.com/images%2Fcha-suyeon%2Fpost%2Fd7ddc0d2-23b6-41fe-b406-3c1284634e22%2Fimage.png">
유사한 테스크를 여러 프로세서가 동시에 수행하는것

멀티 코어 환경에서 멀티 프로세스(단일스레드)나 단일프로세스내 멀티스레드를 활용한다<br>
이는 실제로 물리적으로 여러작업이 동시에 실행되는것

    **동시성 프로그래밍과 병렬성 프로그래밍의 차이**
    동시성 프로그래밍과 병렬성 프로그래밍 모두 비동기 동작을 구현할 수 있지만 그 동작 원리가 다르다.
    
    - 동시성 : 싱글 코어, 멀티 코어에서 모두 구현 가능.
    ex. 하나의 커피머신에 커피를 받기 위한 N개의 대기열 -> 서로 번갈아 가며 커피를 받아감.

    - 병렬성 : 멀티 코어에서만 구현 가능.
    ex. N대의 커피머신에 커피를 받기 위한 N개의 대기열 -> 각 커피머신마다 하나의 줄을 가지고 있어 각각의 줄마다 커피를 받아감.

## 비동기와 동시성에 대한 정리
비동기과 동시성은 완전히 다르다
- 비동기 : **작업을 보내는 스레드**에 관련된 개념 (작업을 보낸 스레드가 작업의 응답을 기다릴지 말지 결정)
- 동시처리 : 메인스레드에서 작업을 보낼때 **작업을 받은 스레드**가 1개냐 여러개냐를 따지는 개념
