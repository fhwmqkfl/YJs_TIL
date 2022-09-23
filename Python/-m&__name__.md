# -m 실행옵션과 __name__

> ‘python script.py’ VS ‘python -m script’ <br>
> ⇒ script.py를 실행시킨다 VS scipt라는 모듈을 sys.path에서 찾아 실행시킨다!

## Intro

```python
# add_border.py 파일 생성
import sys

def print_with_border(s):
    print('*' * (len(s) + 4))
    print('* ' + s + ' *')
    print('*' * (len(s) + 4))
    
print_with_border(sys.argv[1])

# 실행 결과
➜   python3 add_border.py 'Beautiful world!'
********************
* Beautiful world! *
********************
```

위의 add_bother.py를 main.py에 import함

```python
# main.py
import add_border
add_border.print_with_border('Wonderful day!')

# 실행 결과
➜   python3 main.py
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    import add_border
  File "/Users/ceongjeein/Workspace/pydev/add_border.py", line 8, in <module>
    **print_with_border(sys.argv[1])**
**IndexError: list index out of range
```

위 에러 발생의 이유 : `sys.argv[1]` 이 없음

### 위의 로직을 모듈화하는 작업진행

```python
# add_border.py

import sys

def print_with_border(s):
    print('*' * (len(s) + 4))
    print('* ' + s + ' *')
    print('*' * (len(s) + 4))
    
# add_border_exec.py

import add_border
import sys

add_border.print_with_border(sys.argv[1])

# main.py

import add_border

add_border.print_with_border('Wonderful day!')
```

잘 돌아가는데 앞에 코드 중 add_border.py를 아래와 같이 수정해서 같은 기능은 같이 있게 만들어주자

```python
# add_border.py 수정
import sys

def print_with_border(s):
    print('*' * (len(s) + 4))
    print('* ' + s + ' *')
    print('*' * (len(s) + 4))

if __name__ == '__main__':    
    print_with_border(sys.argv[1])

# 실행
➜   python3 add_border.py 'Beautiful world!'
********************
* Beautiful world! *
********************

➜   python3 main.py
******************
* Wonderful day! *
******************

# 모듈처럼도 작동 잘하고 add_border.py가 혼자 스크립트로도 작동을 잘함!!
```

## 자 이걸 왜쓸까?

스크립트 실행시 자동으로 sys.path에 그 스크립트가 실행되는 디렉토리가 추가된다. 

`__name__`이 여기서 사용되는데

- `__name__`
    
    현재 파일이 직접 실행됐다면 __name__의 값은 __main__이 되고, 다른 파일에 의해서 import 됐다면 모듈의 이름이 됨
    
    - python3 add_border.py라고 실행됐다면 __name__ == '__main__'이
    - 어딘가에서 import add_border.py를 만나서 실행됐다면, __name__ == 'add_border'가 됨


-m옵션을 사용시 스크립트가 위치한 디렉터리가 sys.path에 추가되기 때문에 아래와 같이 실행할 수 있음
```python
➜   python3 -m add_border 'Beautiful world!'
********************
* Beautiful world! *
********************
```
**add_border.py**가 아닌 그냥 **add_border**를 사용(-m이 원하는 값은 파일명이 아니고 `모듈 이름`이기 때문!)<br>
Python이 환경마다 다르게 설치되어있는 add_border 모듈을 찾는 일을 해주기 때문에 문제를 해결할 수 있음
> 많은 모듈이 __**name__** == '**main**' 을 사용해서 모듈에 실행 가능한 기능을 추가해서 배포 중