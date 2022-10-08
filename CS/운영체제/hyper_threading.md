# 하이퍼 스레딩(Hyperthreading)
> 인텔에서 발표한 명칭. 원래 학계&업계에서는 **SMT/Simultaneous Multi-Threading(동시 멀티스레딩)** 이라 불린다<br>
> 인텔과 CPU 점유율을 경쟁하던 CMD에서 듀얼코어를 출시했고 이에 
> <img src="https://w.namu.la/s/d5094b4ebcf6bbbec4dbcae7f57d4140b60a1a5ab08cb950ba5418bb4577583ae98549f662f68cc7994f56a63760058fa1474d2606b51c3760ec1f64f37bc94b7a528d1f57e79088621da6d3973a259b20084939425983b39f430ea53276931a">

## Intro
CPU는 코어라는 개념을 가진다.<br>
MacOS에서 현재 사용중인 코어는 아래와 같다
```
sysctl hw.physicalcpu hw.logicalcpu

hw.physicalcpu: 4
hw.logicalcpu: 8
```

physicalcpu(물리적cpu)와 logicalcpu(논리적cpu)의 갯수가 2배차이가 난다.<br>

## Hyper Threading의 개념
인텔이 구현한 기술로, 물리 실행 장치 한 개에 가상 실행 장치(virtual 또는 logical core) 두 개를 할당해 성능을 높이려는 기술이다<br>
코어 한대당 스레드가 두개씩 추가된다. 따라서 물리적인 코어의 수 * 2로 운영체제는 인식한다

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FIYnZy%2FbtqHR6jkXUp%2Fo2ceFP0NN9KwzPGbkzzTqK%2Fimg.png">
세번째 이미지가 하이퍼 스레딩이 적용된 부분이다. 

## 장점
병렬 연산작업(일상에서 하는 일들, 영상편집, CAD)에서는 하이퍼 스레딩이 효율적이다.

## 단점
동일한 연산을 주로 하는 프로그램에서는 오히려 성능이 줄어들 수 있다.
또한 스레드를 파이프라인에 잘 분배하도록 하는 회로가 있기때문에, 발열량이 증가 한다.
