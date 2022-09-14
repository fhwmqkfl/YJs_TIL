# 큐(Queue)

해당 내용은 이전에 [코드](https://github.com/fhwmqkfl/algorithm/blob/master/udemy/stack/queue.py)작성 경험이 있다.

> like 대기줄, **선입선출(FIFO, First-In-First-Out)**


파이썬에서 큐를 구현할 때 리스트를 이용한다. 
* 데이터의 입력(push) : append()
* 데이터의 출력(pop) : pop(0) => `인덱스 0`을 이용해 가장 앞의 값을 빼낸다

> 리스트를 이용한 큐는 출력(pop)시 리스트의 원소위치를 이동해야해 시간복잡도가 O(N)이된다.<br>
> 그래서 `collections`모듈에서 제공하는 `deque`구조를 활용해 구현하는 케이스가 많다

```python
from collections import deque

#큐 구현을 위해 deque라이브러리 사용
queue = deque()

# 5 -> 2 -> 3 -> 7 -> 삭제() -> 1 -> 4 -> 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) #먼저 들어온대로
>>> deque([3,7,1,4])

queue.reverse()

print(queue) #나중에 들어온 대로
>> deque([4,1,7,3])

print(list(queue)) #리스트 자료형 반환
>> [4,1,7,3]
```