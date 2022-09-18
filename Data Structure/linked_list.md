# Linked List(연결 리스트)

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20220829152206/LLdrawio.png">

## 개념 및 용어 정리
각 데이터에 저장되어 있는 다음 데이터의 주소에 의해 연결되는 방식<br>
데이터의 물리적인 순서와는 상관없이 **포인터**를 사용해 논리적 순서로 연결<br>

> 연결 리스트의 구조 : 저장된 데이터 값과 다음데이터가 있는 메모리주소로 이루어진 노드가 존재

* 장점 : 물리적 순서를 맞추는 작업이 필요없음. 삽입&삭제 행위 자체는 매우 빠르게 진행됨
* 단점 : 임의의 데이터에 접근시 `순차접근`만 가능해 시간이 오래걸림. 포인터를 통한 참조이기 때문에 추가적 메모리 공간이 발생

자료를 논리적인 순서대로 메모리에 연속하여 저장하는 구현방식. 데이터의 **논리적인 순서와 기억장소에 저장되는 물리적인 순서가 일치**하는 구조이다<br>
프로그래밍에서 선형 리스트는 `배열`이 사용된다
* 장점 : 인덱스로 접근이 가능하기때문에 접근속도가 빠름(임의 접근(random access)방식 사용), 연속된 메모리 공간에 존재해 관리가 쉬움.
* 단점 : 배열의 메모리 사용 문제를 그대로 가져온다. 삽입&삭제 연산 후 데이터 사이의 주소를 유지하기위해 원소를 정비하는 시간이 추가로 소요됨

## 연결 리스트의 시간 복잡도
### 데이터 탐색
순차 접근 방식을 이용하기 때문에 중간의 데이터를 찾기위해 처음부터 순차적으로 탐색된다. 시간복잡도는 `O(N)`이다.

### 데이터 추가
순수하게 **추가**라는 자체의 시간복잡도는 `O(1)`!<br>
추가하려는 데이터의 위치까지 이동해야하기 때문에 이부분을 고려한 시간복잡도는 `O(N)`이다.<br>
만약 맨 앞에 추가한다면 시간복잡도는 `O(1)`이 된다

### 데이터 삭제
데이터를 삭제하는 경우도 추가와 동일하다.<br>
맨 앞의 값을 삭제한다면 시간복잡도는 `O(1)`이나, 삭제데이터의 위치가 맨 앞이 아니라면 `O(N)`의 시간복잡도를 가진다.<br>


## 연결 리스트의 종류
### 1. 단순 연결 리스트(Simple Linked List)
노드가 하나의 링크 필드에 의해 다음 노드와 연결되는 구조로 단방향 순환 구조이다

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdPDK9S%2Fbtq8jKb1wyY%2Fv56nhxMUxOlvaBxly8kFPK%2Fimg.png">

### 2. 이중 연결 리스트(Double Linked List)
노드가 링크 필드 두개에 의해 이전 노드와 다음노드로 연결되는 구조

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FABsnt%2Fbtq8lwEguVl%2FidiZt8uDkx4p4Kl4TDCTL1%2Fimg.png">


> [linked list](https://github.com/fhwmqkfl/algorithm/tree/master/udemy/LinkedList) & [Double Linked List](https://github.com/fhwmqkfl/algorithm/tree/master/udemy/DoubleLinkedList)<br>
> udemy강의로 구현했던 커밋 내역