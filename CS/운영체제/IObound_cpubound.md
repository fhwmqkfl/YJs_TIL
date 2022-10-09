# I/O bound & CPU bound

## Intro
- CPU(Central Processing Unit) : 프로세스의 명령을 해석하고 실행하는 장치
- I/O(Input/Output) : 파일을 읽고 쓰거나 네트워크의 어딘가와 데이터를 주고받음 / 입출력 장치와 데이터를 주고받는것

- 버스트(burst) : 어떤 현상이 짧은 시간에 집중적으로 일어나는 일
- CPU 버스트 : 프로세스가 CPU에서 한번에 연속적을 실행되는 시간
- I/O 버스트 : 프로세스가 I/O작업을 요청하고 그 결과를 기다리는 시간

프로세스는 CPU버스트와 IO버스트의 연속이다!
<img src="https://t1.daumcdn.net/cfile/tistory/991E694D5C4CC87D0F">

## CPU bound? I/O bound?
<img src="https://velog.velcdn.com/images%2Fzzarbttoo%2Fpost%2F47c3d1e4-9934-49c5-b085-661a596a087f%2Fimage.png">

- CPU bound 프로세스 <br> CPU 버스트가 많은 프로세스로 동영상 편집 프로그램이나 연산작업이 많은 머신러닝 프로그램이 대표적인 예이다
- I/O bound 프로세스 <br> IO 버스트가 많은 프로세스로 일반적인 백엔드 API서버가 대표적인 예이다.<br> HTTP프로토콜로 통신시 DB나 캐시 서버에 데이터를 요청하는게 IO바운드의 예시이다


### CPU bound 프로그램에서 적절한 스레드의 수는 몇개일까?
Goetz Recommends -> `number of CPUs + 1`

> 듀얼코어 CPU에 CPU bound 프로그램일 경우 스레드는 몇개일까? <br>
> 코어의 갯수만큼 혹은 컨텍스트스위칭을 고려해 1개정도 추가를 하는게 좋다고 봄
 
### IO bound 프로그램에서 적절한 스레드의 수는 몇개일까?

여러 상황에 맞춰 적절한 스레드 수를 찾아야한다. <br>

> api서버가 `thread per request`방식(요청이 있을때마다 전담 스레드를 배정)이라면<br>
> 몇개의 스레드를 미리 만들어 놓을지 여러 상황을 고려해 결정하는 것이 중요