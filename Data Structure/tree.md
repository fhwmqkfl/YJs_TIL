# Tree(트리)

## 개념 및 용어 정리
트리(tree)란 계층적인 자료를 표현하는 데 이용되는 자료구조이다. <br>
실제 나무를 거꾸로 한 것과 같은 모양을 하고 있기 때문에 트리라고 부른다

<img src="https://miro.medium.com/max/1400/1*F78cM2sJ5Ix83EBWpPoNlw.png">

* 노드 : 트리의 구성요소로 트리는 한 개 이상의 노드로 이루어져 있다
* 루트 노드 : 가장 상위의 노드
* 서브 노드 : 루트 노드를 제외한 나머지 노드
* 단말 노드 : 자식 노드가 없는 노드 (<-> 비 단말 노드)


* 간선(edge) : 루트와 서브트리를 연결하는 선
* 차수(degree) : 노드가 가지고 있는 자식 노드의 개수
* 트리의 차수 : 트리가 가지고 있는 노드의 차수 중 가장 큰 차수


* 노드의 레벨 : 트리의 특정 깊이를 가지는 노드의 집
* 트리의 높이(height) : 루트 노드에서 가장 깊숙히 있는 노드의 깊이


## 특징
1. 그래프의 한 종류이다.
2. 노드가 N개인 트리는 항상 N-1개의 간선을 가진다
3. 루트에서 어떤 노드로 가는 경로는 유일하다
4. 트리는 항상 루트에서부터 시작된다
5. 부모노드 밑에 여러 자식노드가 연결되고, 그 자식노드의 자식노드가 연결되는 `재귀적 형태`의 함수구조이다.

## 트리의 종류
> [엔지니어 대한민국 - tree의 종류](https://www.youtube.com/watch?v=LnxEBW29DOw&ab_channel=%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD)<br>
> 위의 알고리즘 영상을 참고함
* 이진 트리(binary tree)
* 이진 탐색 트리(binary search tree)
* 포화 이진 트리 vs 완전 이진 트리
* 균형(red-black tree) vs 비균형
