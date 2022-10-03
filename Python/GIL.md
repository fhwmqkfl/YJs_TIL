# GIL, Global Interpreter Lock
> 출처 : https://realpython.com/python-gil/

## GIL 개념
> In CPython, the global interpreter lock, or GIL, is a mutex that protects access to Python objects,<br>
> preventing multiple threads from executing Python bytecodes at once. <br>
> This lock is necessary mainly because CPython's memory management is not thread-safe.
> 
>출처 : [python 위키](https://wiki.python.org/moin/GlobalInterpreterLock)

파이썬 객체들에 대한 접근을 보호하는 일종의 `뮤텍스(Mutex)`로, 여러 스레드가 동시에 파이썬 코드를 실행하지 못하도록 하는 Lock. 

3개의 스레드가 있을경우 GIL에 의한 실행은 아래와 같다.
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbAMe0O%2FbtqHOZLSxjm%2Fg3KOLQOBuZAFZQ5tz5OrK0%2Fimg.png">
멀티스레드의 경우 스레드 context switching이 매번 일어나 싱글스레드로 실행하는것보다 더 시간이 오래걸릴 수 있다.

### 실제 파이썬 코드
```python
import random
import threading
import time

def working():
    max([random.random() for i in range(10000000)])


# thread 1
s_time = time.time()
working()
working()
e_time = time.time()

print("case 1", f'{e_time - s_time:.5f}')

# thread 2
s_time = time.time()
threads = []
for i in range(2):
    threads.append(threading.Thread(target=working))
    threads[-1].start()

for t in threads:
    t.join()

e_time = time.time()
print("case 2", f'{e_time - s_time:.5f}')

"""
결과 
case 1 3.20001
case 2 3.29371 -> 멀티 스레드가 더 느리다
"""
```

## GIL 사용 이유
파이썬은 모든것이 객체로 이루어져있다.<br>
객체로써 모두 **참조횟수(Reference count)** 를 저장하기위한 필드가 있으며, 이를 참조해 **GC(Garbage Collection)** 가 동작한다. <br>
만약 여러개의 스레드가 인터프리터를 동시에 실행하게 되면 `Race Condition`이 발생하게 된다. Race Condition이 생기면 값이 올바르게 적용되지 않을 가능성이 있다(Thread Safe하지 않음)<br>

Race Condition가 발생하게되면 참조횟수가 정확해지지 않고, GC가 정상적으로 동작하지 않을 확률이 높아진다.<br>
파이썬은 이러한 부분을 사용자가 고려해 작성해 일어날 위험을 안고가는 대신, GIL을 선택했다.

## python에서 멀티스레딩이 느리지 않을때
일반적으로 CPU 연산의 경우 멀티스레드보다 싱글스레드가 효율성이 좋다(GIL영향)<br>
하지만 외부연산(I/O, Sleep 등)의 경우는 CPU의 연산작업이 아니기 때문에 멀티스레딩의 효율성이 더 좋다. 

## 파이썬에서 병렬 처리를 하려면?
가장 널리 사용되는 방법은 스레드 대신 다중 프로세스를 처리하는 방식이다. `multiprocessiong` 모듈을 사용해 구현할 수 있다.
