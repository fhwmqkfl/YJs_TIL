# python에서 스레드를 다루는 방법

# 1. 기본 모듈 thread, threading 사용
import threading
import time


class Worker(threading.Thread):
    def __init__(self, name):
        # 다른 클래스의 속성 및 메소드를 자동으로 불러와 사용가능하게 해줌
        super().__init__()
        self.name = name

    def run(self):
        print("sub thread start ", threading.currentThread().getName())
        time.sleep(3)
        print("sub thread end ", threading.currentThread().getName())


print("main thread start")

for i in range(5):
    name = "thread {}".format(i)
    # sub thread 생성
    t = Worker(name)
    # sub thread run호출
    t.start()

print("main thread end")


"""
결과

main thread start
sub thread start  thread 0
sub thread start  thread 1
sub thread start  thread 2
sub thread start  thread 3
sub thread start  thread 4
main thread end
sub thread end  thread 0
sub thread end  thread 1
sub thread end  sub thread end  thread 2
thread 4
sub thread end  thread 3

"""

# 서브스레드가 0,1,2,3,4순으로 생서되었으나 끝나는 순서는 다르다

# 2. 데몬 스레드
# 메인스레드가 종료되면 실행상태와 상관없이 종료되는 서브스레드를 의미.
# 실제로 메인스레드가 종료되면 서브스레드와 상관없이 종료되어야 하는 경우가 많음


class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name            # thread 이름 지정

    def run(self):
        print("sub thread start ", threading.currentThread().getName())
        time.sleep(3)
        print("sub thread end ", threading.currentThread().getName())


print("main thread start")
for i in range(5):
    name = "thread {}".format(i)
    t = Worker(name)                # sub thread 생성
    t.daemon = True
    t.start()                       # sub thread의 run 메서드를 호출

print("main thread end")

""" 
결과
main thread start
sub thread start  thread 0
sub thread start  thread 1
sub thread start  thread 2
sub thread start  thread 3
sub thread start  thread 4main thread end
"""