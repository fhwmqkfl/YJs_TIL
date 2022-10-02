# 1. 메인 프로세스

import multiprocessing as mp
import time

if __name__ == "__main__":
    proc = mp.current_process()
    print(proc)
    print(proc.pid)

# <_MainProcess name='MainProcess' parent=None started>
# 3371

# 2. 프로세스 스포닝
# 부모 프로세스가 운영체제 요청해 자식 프로세스를 새로 만들어 내는 과정 : 스포닝

# process 클래스의 인스턴스 생성후 start()메소드 호출하는 방식


def worker():
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)
    time.sleep(5)
    print("SubProcess End")


if __name__ == "__main__":
    # main process
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)

    # process spawning
    p = mp.Process(name="SubProcess", target=worker)
    p.start()

    print("MainProcess End")

"""
결과
MainProcess
4448
MainProcess End
SubProcess
4451
SubProcess End
"""