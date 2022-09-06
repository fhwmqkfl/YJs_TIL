# 파이썬의 연산자(bool, 비교, 논리)
    연산자(operator) : 연산을 수행하는 기호(+,-,*,/ 등)

## Intro
파이썬은 조건부 논리를 이용해 **여러 조건에 따라 다른 작업을 수행**하는 프로그램을 작성 할 수 있다<br>
컴퓨터 프로그래밍에서 `조건부`는 흔히 하나의 값이 다른것과 같은지, 크고 작은지처럼 **두개의 값을 비교하는 형태**이다.
* 비교 연산자: 두 값의 관계를 판단
* 논리 연산자: 두 값의 논릿값을 판단

## Boolen
자료형의 한 종류이다. 이 자료형은 두가지의 데이터를 가지는데, `True`와 `False`다.
___
## 비교 연산자(compare operator)

<img src="https://mblogthumb-phinf.pstatic.net/MjAxNzA3MThfMjMw/MDAxNTAwMzA4MjIwMjQ2.MPFU3AZHD3Nt55rFcU0gFoRcTPXYM41kyhe1OqDfPqAg.2-ZVQQbQonKM7CUYYSger4jwZLUOEljdv9FCs79ePWwg.PNG.heartflow89/image.png?type=w800">
두 값의 관계를 판단하는 연산자로 판단 결과는 항상 불리언값을 가진다

```python
1 == 1
# True

3 > 5
# False
```

파이썬에서는 문자열이 사전순으로 정렬되어있어 문자열에도 사용이 가능하다
```python
"a" == "a"
# True

"a" > "b"
# False
```
___
## 논리 연산자(Logical Operators)
두 개의 논리 값을 연산하여 참 또는 거짓을 결과로 얻는 연산자를 의미한다.

#### 논리 연산자의 우선순위
    not > and > or

### 1. and
* 두 값이 모두 True 일 때만 True가 된다
* 만약 하나라도 False라면 False가 된다

### 2. or
* 두 값 중 하나라도 True이면 True가 된다
* False는 유일하게 두값 모두 False여야 한다

### 3. not
* 단일 표현식의 논릿값을 뒤집는다
* not True = False
* not False = True

---

## 비교연산자와 논리연산자의 우선순위

#### 우선순위는 아래와 같다
    비교 연산자 (is, is not, ==, != , <, >, <=, >= )
    논리 연산자 (not, and, or)

비교 연산자와 논리 연산자의 우선순위를 고려하지 않으면 예상하지 못한 상황이 발생하니 주의!
```python
not True == False
# True

False == not True
#  File "<stdin>", line 1
# 	False == not True
# 			  ^
# SyntaxError: invalid syntax

False == (not True)
# True
```