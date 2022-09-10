# 스택(Stack)

> like 박스 쌓기, **선입후출, 후입선출** 

```python
stack = []

# 5 -> 2 -> 3 -> 7 -> 삭제 -> 1 -> 4 -> 삭제
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
>>> [5,2,3,1]

print(stack[::-1])
>>> [1,3,2,5]
```

파이썬에서는 스택을 위해 별도의 라이브러리를 사용할 필요가 없다. 기본 리스트에서 **append(), pop()**을 이용하면 스택 자료구조와 동일하게 동작한다.