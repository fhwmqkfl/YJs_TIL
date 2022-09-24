# Iterable 객체와 Iterator 객체


## Iterator 객체
반복자, 객체가 가진 각 요소에 순차적으로 접근할 수 있게 해주는 도구로 파이썬에서는 iter()함수를 통해 얻을 수 있다.<br>
> * iter() : 반복자를 리턴
> * next() : 반복자가 가리키는 값을 반환하고, 반복자는 다음 요소로 이동
> * reversed() : 뒤에서 부터 앞으로 순회하는 역 반복자 리턴 

```python
ds = [1,2,3,4]

# iter 객체 획득
ir = iter(ds) 

next(ir) # 1

next(ir) # 2

next(ir) # 3

next(ir) # 4
```

순회가 끝난 iterator에 `next()`를 사용시 **StopIteration**에러가 발생한다

만일 예외가 발생하는 것을 막고 싶다면 아래의 두가지 방법을 이용한다
* try ~ catch 문으로 감싸 예외 발생을 별도로 처리
* next() 표준함수의 두번째 인자를 이용. `next(ds, -1)` -> 에러대신 '-1' 리턴

## Iterable 객체

> iterator 객체를 얻을 수 있는 리스트와 같은 객체
 ```python
string = 'ABCD'
num1 = 10  # object in not iterable
num2 = 3.4  # object in not iterable
```
위 예시에서 string은 문자열로 반복자를 이용할 수 있으나 num1, num2는 예외가 발생한다.<br>
string 처럼 iter()함수로 반복자를 리턴할 수 있는 타입을 iterable 타입이라고 하며, <br>
파이썬에서는 **str, list, tuple, dictionary, set, range** 같은 타입이 iterable 타입이다

> iterable 객체 : iter 함수에 인자로 전달 가능한 객체 <br>
> iterator 객체 : iter 함수가 생성해 반환하는 객체

## for 루프와 iterable 객체
for 루프도 사실 iterable객체를 순회한다
```python
for i in [1,2,3]:
    print(i, end=' ')

> 1 2 3 
```

### for 루프와 iterator 객체는?
iterator 각체를 두어도 정상적으로 동작한다
```python
for i in iter([1,2,3]):
    print(i, end=' ')

> 1 2 3 
```
iter함수에 iterator 객체를 전달하면 전달된 iterator 객체를 그대로 돌려줌

iterable 객체가 와야하는 자리에는 iterator 객체도 올 수 있다!
