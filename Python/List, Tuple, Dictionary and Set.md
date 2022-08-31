# CollectionType(List, Tuple, Dictionary, Set) 비교

---
## 1.  List (순서 O, 중복 O, 변경 O)
```python
ex = [1,2,3,4,'a','b','c']
```
* 여러개의 변수를 담을 수 있는 데이터 구조
* mutable(변경가능) → 생성,삭제,수정 기능
* 문자열 하나하나를 인덱스로 가져오는 것처럼 리스트 또한 인덱스를 통해 순회한다

> **sort() vs sorted()**
> * sort() : 리스트 그 자체가 정렬되는것
> * sorted() : 정렬된 리스트 복사본이 반환된다

파이썬의 시퀀스 자료구조인 리스트는 Java,C언어에서 사용하는 배열(Array)과 가장 비슷하다고 한다<br>

(리스트를 이용한 스텍, 큐 구현은 이전에 유데미 강의로 본적이 있다.)
1. [리스트를 이용한 스택](https://github.com/fhwmqkfl/coding_test/blob/main/udemy/stack/queue.py)
2. [리스트를 이용한 큐](https://github.com/fhwmqkfl/coding_test/blob/main/udemy/stack/stack.py)

---
## 2. Tuple (순서 O, 중복 O, 변경 X)
```python
ex = (1,2,3,4,'a','b','c')
```
* 리스트와 마찬가지로 여러 변수를 담을수 있는 구조이다
* immutable(변경 불가능) -> 수정이 불가능하다
* 리스트처럼 인덱스가 있어 순회가 가능하다

> **튜플 패킹 vs 언패킹**
> * 패킹 : 값을 튜플로 묶는 경우
> * 언패킹 : 튜플의 왼쪽에 각 튜플의 원소를 바인딩할 변수를 적어주면 각 변수가 튜플의 원소를 가져감.<br> 만일 변수 갯수가 맞지 않으면 애스터리스크(*)를 이용해<br>
> 리스트로 나머지 값을 리스트로 나오게 할 수 있음
> ```python
> data = (1, 2, 3)
> a,b,c = data
> # a = 1, b = 2, c = 3
> 
> unpacking = (1,2,3,4,5,6)
> a,*b,c =  unpacking
> # a=1, b=[2,3,4,5], c=6
> ```
---
## 3. Dictionary(순서 X, 중복 X, 변경 O)
```python
ex = {"name":"fhwmqkfl","age":30}
```
* 키와 value를 갖는 데이터 구조로. 키는 내부적으로 hash값으로 저장된다
* mutable(변경가능) → 생성,삭제,수정 기능
* 인덱스가 존재하지 않는다
* 딕셔너리의 key값으로 리스트는 올수 없다. 그러나 튜플은 사용가능하다(immutable)

> **ex.get('name') VS ex['name']**
> * 존재하지 않는 키를 가져오려고 할 경우
> 1. get() : None이 반환됨
> 2. [] : KeyError 반환

---
## 4. Set(순서 X, 중복 X, 변경 O)
```python
ex = {1,2,3}
```
* Dictionary의 키만 활용하는 구조로 이해
* 수학에서 집합과 동일한 개념
* 인덱스가 없다

> **수학에서 집합과 동일하게 사용된다**
> * union()
> * intersection()
> * difference()
> * issubset()