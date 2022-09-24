# 제너레이터(generator) 함수, 표현식

## 제너레이터(generator)
iterator 객체의 한 종류이다. 좀더 특이한 형태를 가지고 있다

## 제너레이터 함수
```python
def gen_num(): # 제너레이터 함수 정의
    print("first")
    yield 1
    print("second")
    yield 2
    print("third")
    yield 3

gen = gen_num() # 제너레이터 객체 생성

print(type(gen))        # <class 'generator'>, 정수가 아님
```

* 함수에서 return 이 아닌 `yield` 키워드를 이용해 반환한다
* 반환 값이 **generator 객체**다
* iterator와 유사하게 동작한다

위의 gen_num을 `next()`로 호출하면 yield의 첫 부분까지 호출된다
```python
next(gen)

>> first
>> 1
```
next(gen)를 이어 두번 실행하면 second, 2 / third, 3 가 반환된다

## 제너레이터의 기능적 특징
1. Lazy Evaluation<br>
   함수의 호출 이후 그 실행의 흐름을 next()가 호출될때 까지 미룬다
2. 함수 내부 로컬 변수 유지<br>
   일반 함수는 return문을 통해 함수를 **종료**하게 되어 내부 로컬변수들이 모두 해제된다.<br>
   제너레이터 함수의 경우 yield를 통해 **중단**되어 내부의 로컬변수가 유지된채 다음 호출때 다시 사용 할 수 있다
3. 다양한 함수 진입점
   일반함수의 경우 함수 호출시 함수의 처음부터 시작되지만 제너레이터는 yield의 중단시점부터 다시 시작된다
4. 제너레이터 객체는 반환할 값들을 미리 만들어 두지 않기 때문에 메모리 공간의 크기를 리스트에 비해 적게 사용한다


### yield from
파이썬 3.3버전 이상에서 사용할 수 있는 문법.
```python
def get_nums():
    ns = [0,1,0,1,0,1]
    """아래 부분을"""
    for i in ns:
        yield i

g = get_nums()

next(g) # 0

next(g) # 1

```
`for i in ns: yield i` 이부분을 `yield form ns`로 간단히 쓸 수 있음!

## 제너레이터 표현식
제너레이터 표현식은 제너레이터 함수와 마찬가지로 제너레이터 객체를 생성하는 방법으로, 함수를 만들지 않고 **표현식**으로 제너레이터를 만드는 문법이다
```python
# 제너레이터 함수
def foo():
    for i in range(0, 100, 5) :
        yield i

g1 = foo()

# 제너레이터 함수
g2 = ( i for i in range(0, 100, 5) ) 

print(next(g2))
print(next(g2))
print(next(g2))
```

제너레이터 표현식의 방법이 리스트 컴프리헨션과 거의 동일하다()