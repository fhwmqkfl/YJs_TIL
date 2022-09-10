# sort() vs sorted()

> 파이썬에서 리스트를 정렬할 상황에서 `sort()`와 `sorted()` 어느것을 써야할지 항상 고민인데, 한번 정리해보자!

## 1. sort() -> 메소드
> 리스트명.sort([reverse=True|False],[key=function])

**리스트의 메소드**이다<br>
리스트 원본값을 직접 수정한다.

#### 예시

```python
a1 = [6, 3, 9]

print("a1: ", a1) # a1: [6, 3, 9]

a2 = a1.sort() # 원본이 정렬된다

print("a1: ", a1) # a1: [3, 6, 9]
print("a2: ", a2) # a2: None
```

위의 예시를 보면 변수 a2 리턴값이 None이다<br>
-> 정렬된 값은 리턴되지 않습니다. 

## 2. sorted() -> 함수
> sorted(리스트명)

파이썬의 **내장함수**이다<br>
리스트 원본 값은 그대로이고 새로운 리스트에 정렬 값을 반환한다
​
```python
b1 = [6, 3, 9]
print('b1:', b1) # b1: [6, 3, 9]
b2 = sorted(b1) # 원본은 유지, 새로운 리스트 생성

print('b1:', b1) # b1: [6, 3, 9]
print('b2:', b2) # b2: [3, 6, 9]
b1: [6, 3, 9]
```
​
## sort(), sorted()의 속도비교
* list.sort()는 복사본을 만들 필요가 없으므로 sorted()보다 빠르다. 

> 파이썬 3 timeit을 활용한 속도 차이
```python
timeit.repeat("next(shuffled_iter).sort()", setup=setup, number = 1000)
[2.797430992126465, 2.796825885772705, 2.7744789123535156]

timeit.repeat("sorted(next(shuffled_iter))", setup=setup, number = 1000)
[2.675589084625244, 2.8019039630889893, 2.849375009536743]
```