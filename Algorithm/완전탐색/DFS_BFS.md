# DFS & BFS(그래프 탐색)

## Intro..
첫 정점에서 시작해 그래프에 존재하는 모든 쩡점을 모두 한번씩 방문하는 것을 `그래프 탐색`이라고 한다<br>
그래프를 탐색하는 방법은 **깊이 우선 탐색(DFS)**와 **너비 우선 탐색(BFS)** 두 가지가 있다

<img src="https://blog.kakaocdn.net/dn/cFgEJ6/btqKmoJkq5a/pwm3O8T4rERuL4wSTrkgnK/img.gif">

## 1. 깊이 우선 탐색/DFS(Depth-First Search)

그래프에서 깊은 부분을 우선적으로 탐색하는 방법이다. 최대한 깊이 가고, 더이상 갈 곳이 없다면 이전 정점으로 돌아가는 방식으로 그래프를 순회한다.<br>
`재귀함수` 또는 `스택자료구조`을 통해 구현되며 **모든 정점을 방문하고 싶을 때** 사용된다고 한다

> => 같은 그래프라고 해도 재귀함수와 스텍을 이용한 결과가 다를수 있다는점..!([출처](https://www.youtube.com/watch?v=_hxFgg7TLZQ&ab_channel=%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD))->추가 정리예정

#### 동작과정
1. 탐색 시작 노드를 스택에 삽입하고 방문처리를 한다
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문처리를 한다.<br> 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 2번의 과정을 더이상 수행할 수 없을때까지 반복한다.

```python
#DFS매서드 정의
def dfs(graph, v, visited):
	#현재 노드를 방문처리하기
	graph[v] = True
	print(v, end='  ')
	#현재 노드와 연결된 다른 노드를 재귀적으로 방문
	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)

#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원리스트)
graph =[
	[],
	[2,3,8],
	[1,7],
	[1,4,5],
	[3,5],
	[3,4],
	[7],
	[2,6,8],
	[1,7]
]

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원리스트)
visited = [False] * 9

#정의된 DFS함수 호출
dfs(graph, 1, visited)

# 1 2 7 6 8 3 4 5
```

## 2. 너비 우선 탐색/BFS(Breadth-First Search)

기준 정점에 인접한 모든 정점을 방문후 다음 뎁스로 넘어가는 방법이다<br>
`큐자료구조`를 이용해서 구현하며 **두 노드 사이의 최단 경로 혹은 임의의 경로를 찾고 싶을 때* 많이 사용한다고 한다

#### 동작과정

1. 탐색 시작 노드를 큐에 삽입하고 방문처리를 한다
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리를 한다.
3. 2번의 과정을 더이상 수행할 수 없을때까지 반복한다.


```python
from collections import deque

#BFS매서드 정의
def bfs(graph, start, visited):
	#큐 구현을 위해 deque라이브러리 적용
	queue = deque([start])
	#현재 노드를 방문처리
	visited[start] = True
		#큐가 빌때까지 반복
	while queue:
		#큐에서 하나의 원소를 뽑아 출력
		v = queue.popleft()
		print(v, end=' ')
		#해당 원소와 연결된, 아직 방문하지 않은 원소를 큐에 삽입
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True

#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원리스트)
graph =[
	[],
	[2,3,8],
	[1,7],
	[1,4,5],
	[3,5],
	[3,4],
	[7],
	[2,6,8],
	[1,7]
]

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원리스트)
visited = [False] * 9

#정의된 DFS함수 호출
bfs(graph, 1, visited)
# 1 2 3 8 7 4 5 6
```