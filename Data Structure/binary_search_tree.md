# Binary Search Tree(이진 "탐색" 트리)

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbCe3QD%2Fbtq2ytHuN1Z%2FAi82KHYBlgY01j9hbwjOO1%2Fimg.png">

## 개념 및 특성

`이진 탐색 트리`는 **정렬**된 이진 트리
* 노드의 왼쪽 하위 트리에는 노드의 키보다 작은 키가 있는 노드만 포함된다
* 노드의 오른쪽 하위 트리에는 노드의 키보다 큰 키가 있는 노드만 포함된다
* 왼쪽 및 오른쪽 하위 트리도 각각 이진 탐색 트리다
* 중복된 키를 허용하지 않는다

> 위의 특성때문에 효율적인 검색이 가능하다

---
## 생성 예시 
> [binary search tree](https://github.com/fhwmqkfl/coding_test/blob/main/udemy/Binary%20Search%20Trees/BST.py)<br>
> 예전에 udemy 강의로 한번 본적이 있다
 
#### 50, 15, 62, 80, 7, 54, 11 <br> 위 숫자를 이진 탐색 트리로 만들면 아래와 같다

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcexmJD%2Fbtq2z1DLANG%2FZFiFmM5657r46N4hKKzv91%2Fimg.png">

---
## 이진 탐색 트리의 시간 복잡도
이진 탐색 트리가 균형 상태일 경우 시간 복잡도는 `O(logN)`이다.<br>
만일 불균형 할 경우 `O(N)`이 된다