# 큐(Queue)

> like 대기줄, **선입선출**

파이썬에서 큐를 구현할때는 `collections`모듈에서 제공하는 `deque`구조를 활용한다. 리스트 자료형에 비해 효율적이다.

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