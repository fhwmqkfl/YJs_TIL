# 데코레이터(Decorator)

## 데코레이터의 정의 
함수, 클래스 메소드를 꾸며주는 기능으로<br>
기존함수의 이름과 사용성을 변경하지 않는 선에서 함수의 `추가기능을 구현`할 때 사용되는 기능이다

> 데코레이터는 꾸며주는 함수의 내부에 직접적인 수정이나 로직 변환을 하는건 안된다

## 데코레이터가 필요한 이유
기존에 만들어진 함수가 다른곳에서 이미 많이 사용되고 있을때, <br>
즉 기존 함수의 변경이 어려운 경우 코드를 건드리지 않고 내용을 추가하고 싶을때 사용한다
```python
def a():
    code_1
    code_2
    code_3

def b():
    code_1
    code_4
    code_3
```

위의 예시를 보면 공통적으로 code_1, code_3이 쓰인다. 이럴때 데코레이터를 사용한다

```python
def c(func):
    def wrapper(*args, **kwargs):
        code_1
        result = func(*args, **kwargs)
        code_3
        return result
    return wrapper    

@c
def a():
    code_2

@c
def b():
    code_4
```

## 데코레이터의 동작방식 이해
```python
def say_something(func):
    def inner():
        print("OH~ ", end='')
        func()
    return inner

def emotion():
    print("@_@!")

f = say_something(emotion)
f() # 이 시점에서 f는 inner()함수가 되며 OH~ @_@!를 호출한다
```
`변수 f`에 값을 넣을때 `say_someting()함수`가 실행되는데, OH 메세지를 출력하는 것이 아닌 내부 함수 객체인 inner함수를 리턴한다<br>
그리고 그 **다음줄에서 f()를 통해 inner()함수가 호출**이 되며 값을 출력한다

## @를 이용한 데코레이터
데코레이터 함수를 작성하고 호출하는 것을 간편하게, 그리고 가독성을 높이기 위해 `@를 사용`해 간단하게 나타낼 수 있다
```python
def say_something(func):
    def inner():
        print("OH~ ", end='')
        func()
    return inner

@say_something
def emotion():
    print("@_@!")
```
위의 예시처럼 `@데코레이터명`을 적어주면 내부적으로 데코레이터임을 알 수 있다

## 파라미터가 있는 함수 기반의 데코레이터
```python
def say_something(func):
    def inner():
        print("OH~ ", end='')
        func()
    return inner

@say_something
def emotion(name):
    print(f"{name}!!@_@!")

emotion("coco") # typeerror 발생
```
데코레이터를 사용하는 함수에 매개변수가 생기면 TypeError가 발생한다. <br>
이를 맞추기 위해 say_something함수의 inner(name)로 바꾸면 된다

### 하지만 쓰이는 함수에 따라 가변적으로 매개변수 수가 달라지면..?
<img src="https://img3.daumcdn.net/thumb/R658x0.q70/?fname=https://t1.daumcdn.net/news/202105/24/wngproject/20210524030952302kvps.jpg">

이런 경우 전달인자의 수에 상관 없이 처리가 가능한 가변인자를 이용하여 처리를 하면 된다<br>
파라미터 패킹&언패킹 기능을 사용해 가변인자 함수로 변경해 주면 된다
```python
def say_something(func):
    def inner(*args, **kwargs): # 파라미터 패킹
        print("OH~ ", end='')
        func(*args, **kwargs) # 파라미터 언패킹
    return inner

@say_something
def emotion(name):
    print(f"{name}!!@_@!")

def emotion_sad():
    print("T_T!")
    
emotion("coco") # OH~ coco!!@_@!
emotion_sad() # OH~ T_T!

```