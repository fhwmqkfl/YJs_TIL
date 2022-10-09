# 함수 객체(Function Object) 

## 파이썬은 모든 것을 객체로 관리한다
파이썬에서는 정수, 실수를 포함한 모든 것을 객체로 처리한다.
```python

def func1(n):
    return n

def func2():
    print("Hello!")
    
f = func1
print(f(1)) # 1 출력
    
type(func1) # <class 'function>

type(func2) # <class 'function>
```
위의 예처럼 변수 f에 함수를 지정할 수 있으며 나아가 매개변수로 함수를 전달할 수도 있다<br>
```python

def say():
    print("hello")

def say2():
    print("Hi")

def caller(fct):
    fct() #
    
caller(say)
# hello
caller(say2)
# Hi
```

## 함수가 객체가 되는 원리
실제로 함수를 선언하면 파있너은 내부적으로 함수를 관리하기 위해 PyFunctionObject객체를 생성한다<br>
다른 변수와 동이랗게 레퍼런스 타운터와 객체 타입을 가지는 포인터를 가지고 있고, 함수객체에 필요한 별도의 속성들을 가지고 있다.

### 함수객체의 속성
* `__code__` : 함수의 실행내용을 담고있는 바이트 코드를 가르키는 포인터
* `__doc__` : 함수를 정의할때 첫부분에 멀티라인 주석을 이용해 함수의 설명을 적으면 여기에 저장된다
* `__name__` : 함수의 이름을 출력한다
* `__qualname__` : 클래스의 이름을 포함해 함수의 이름을 출력한다
* `__defaults__` : 함수의 기본 파라미터들을 튜플 형태로 저장한다
* `__kwdefualts__` : keyword argument가 있을시 딕셔너리 형태로 저장한다
* `__annotations__` : 함수 선언시 인자와 리턴값에 대한 타입을 지정할 수 있다. 
    > ```python
    > def add(x:int, y:int) -> int:
    >    return x + y
    > ```
    > help함수 호출시 도움말을 출력하는데 사용된다
* `__closure__` : 내부 함수가 외부 함수의 변수들에 접근하기 위해 외부 함수들의 변수 주소를 저장한다. 

