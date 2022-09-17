# Garbage Collector(GC, 가비지 콜렉터)

## Intro

>메모리 관리는 어떻게 이루어지는가?

C,C++ 같은 저수준의 언어는 malloc()같은 메모리를 관리하는 함수를 이용해 메모리 할당과 해제를 한다.<br>
파이썬을 이용할때 메모리를 직접 생각하면서 코드를 작성하지 않았는데, 이는 메모리관리를 사람이 하지 않고 있는것 <br>
파이썬에서는 `가비지 콜렉터(이하 GC)`가 메모리 관리를 수행한다.


## 가비지 콜렉터 (Garbage Collector)

GC는 프로그램이 더 이상 필요없는 메모리를 제거함으로서 메모리를 비워주는 행위이다.
대표적으로 두 가지 방법이 GC에 사용된다.

1. Reference counting(레퍼런스 카운팅)
2. Generational Garbage Collection(세대별 가비지 컬렉션)


### 1. Reference counting(레퍼런스 카운팅)

레퍼런스 카운팅 방식의 GC는, 어떤 객체가 참조되고 있는 횟수를 카운팅하고 **0**이 될 경우 `메모리에서 해제`하는 방식이다

```python
# sys 라이브러리의 'getrefcount'함수를 통해 실제로 카운트를 확인할 수 있다.
import sys

liAbc = ['a', 'b', 'c']

print(sys.getrefcount('a'))  # 8
print(sys.getrefcount('b'))  # 10
print(sys.getrefcount('c'))  # 13

del liAbc

print(sys.getrefcount('a'))  # 7
print(sys.getrefcount('b'))  # 19
print(sys.getrefcount('c'))  # 12
```

→ 장점 : 구현하기 쉽고, 0이 되자마자 바로 메모리를 비워준다 <br>
→ 단점 : 레퍼런스 카운트를 따로 하기 위한 저장공간이 필요하고, 어떤 메모리를 해제해야 할 지 결정하는 데에 사용되는 알고리즘에 의해 비용이 많이 든다.

### 2. Generational Garbage Collection(세대별 가비지 컬렉션)

파이썬은 사이드로 세대별 가비지 컬렉션이라는 기능을 가지고 있다.
```python
l = []
l.append(l)
del l

"""레퍼런스 카운트 프린트 하면 아래의 결과가 나온다
>> 2
>> 3
>> Traceback (most recent call last):
  File "main.py", line 8, in <module>
    print(sys.getrefcount(l)) 
NameError: name 'l' is not defined
"""
```
위의 예시처럼 순환 참조가되는 경우, 1번 레퍼런스 카운팅 방식에서는 해당 객체에 접근할수 없게된다.<br>
파이썬의 세대별 가비지 컬렉션이 순환 참조를 탐지하고 메모리에서 해제하는 작업을 해준다.

> 순환 참조를 탐지하는 방법
> 
> 순환 참조는 다른 객체를 참조할 수 있는 컨테이너 객체(Tuple, List, Set, Dict, Class)에 의해서만 발생한다.<br>
> 컨테이너 객체들과 참조하는 객체들을 찾아내 카운트를 설정해 순환 참조를 탐지한다

## CG모듈의 사용
CG모듈을 직접 Import해 확인이 가능하다.

* gc.get_count() : 각 세대의 객체 수 확인
* gc.set_threshold() : 세대별 임계치 설정
* gc.collect_generations() : 모든 세대에 대해서 2세대부터 0세대까지의 순서로 확인하고, 임계치 초과시 collect() 호출
* gc.collect() : 가비지 컬렉션 수행하여 순환참조 객체를 메모리에서 해제

> cg의 개념을 알았으나 좀더 구체적인 파이썬 메모리 관리기법 학습이 필요할것 같음
> 
> 관련 레퍼런스 : https://medium.com/dmsfordsm/garbage-collection-in-python-777916fd3189, <br>
> https://velog.io/@swhan9404/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A9%94%EB%AA%A8%EB%A6%AC-%EA%B4%80%EB%A6%AC%EA%B3%BC-%ED%9A%A8%EC%9C%A8%EC%A0%81%EC%9D%B8-%EC%BD%94%EB%93%9C
