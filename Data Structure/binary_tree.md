# Binary Tree(이진 트리)

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FblbjFV%2Fbtq1K3P9Y8v%2FH393OwoRI9lX8N3wrz9OO1%2Fimg.png">
---
## 개념 및 용어 정리
이진 트리는 모든 노드가 **2개의 서브 트리**를 가지고 있는 트리이다(서브 트리 또한 모두 이진 트리여야 한다)
모든 트리의 차수는 `0,1,2` 중 하나이다

---
## 트리 순회
트리 순회란, 트리 자료구조에 포함된 노드들을 특정한 방법으로 한번씩 모두 방문하는 방법이다.
* 전위 순회 : 노드, 왼쪽 자식, 오른쪽 자식 순으로 순회 (A -> B -> C)
* 중위 순회 : 왼쪽 자식, 노드, 오른쪽 자식 순으로 순회 (B -> A -> C)
* 후위 순회 : 왼쪽 자식, 오른쪽 자식, 노드 순으로 순회 (B -> C -> A)
---
## 이진 트리 유형
<img src="https://miro.medium.com/max/1400/1*mWHM-VlMRrmurimEFoDCKQ.png">

### 1. 전 이진 트리(Full Binary Tree)
모든 노드가 0개 or 2개의 자식 노드를 갖는 트리 => 1개의 자식 노드는 X

### 2. 완전 이진 트리(Complete Binary Tree)
마지막 레벨을 제외한 모든 레벨이 완전히 채워져 있는 트리 <br>
=> 마지막 레벨은 왼쪽에서 오른쪽으로 채워져야 한다
* 왼쪽(있음), 오른쪽(없음) => 완전 이진 트리
* 왼쪽(없음), 오른쪽(있음) => 완전 이진 트리가 

### 3. 포화 이진 트리(Perfect Binary Tree)
마지막 레벨까지 모두 2개의 자식 노드를 가진다

> 포화 이진 트리 ⊂ 완전 이진 트리 ⊂ 이진 트리

