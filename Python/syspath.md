# sys.path

>sys.path는 모듈을 import 할 때 모듈을 찾아야할 경로들을 저장해둔 list

## 그럼 sys.path는 어떻게 만들어질까

- 먼저 최초 실행된 Python 스크립트가 위치한 디렉토리를 더함. 이때 interactive shell (python or python3)으로 실행한 경우는 ''(빈 스트링)를 사용
- 환경 변수 중 PYTHONPATH의 값을 가져옴
- 그리고 여기에 OS나 Python 배포판이 설정해 둔 값들을 더함

_스크립트가 실행되는 그 디렉토리를 기준_으로 값이 설정됨

첫번째 값은 `최초 실행시킨 스크립트가 *위치한* 디렉터리`임

```python
#/Users/Workspace/test/main.py
import sys

print('sys.path from main.py')
print('\n'.join(sys.path))

# test1. 스크립트 실행(test디렉토리)
➜  python3 main.py
sys.path from main.py
# 결과
/Users/Workspace/test

# test2. 스크립트 실행(Workspace디렉토리로 이동시킴)
➜  python3 main.py
sys.path from main.py
# 결과
/Users/Workspace
```

## 여기서 나타나는 문제

```python
#main.py
import sys

print('sys.path from main.py')
print('\n'.join(sys.path))
print()

print('__name__ of main.py')
print(__name__)
print()

from module_demo import library
from module_demo import util

#module_demo/library.py
import sys

print('sys.path from library.py')
print('\n'.join(sys.path))
print()

print('__name__ of library.py')
print(__name__)
print()

#module_demo/util
import sys

print('sys.path from util.py')
print('\n'.join(sys.path))
print()

print('__name__ of util.py')
print(__name__)
print()

####여기서 문제 발생 ####
import library
####################
```

위의 파일을 실행하면 

> ModuleNotFoundError: No module named 'library'

라는 에러가 `util.py`에서 발생

### 원인 : sys.path

sys.path의 첫번째 값은 main.py를 실행시킨 `/Users/Workspace/test`<br>
근데 위의 **import library**를 읽게되면 `/Users/Workspace/test/library.py`로 인식하는데 ⇒ 이위치에 library.py 파일이 없음…!<br>
> 정상경로(/Users/Workspace/test/**module_demo**/library.py)

## 해결방법?

### 1. relative import 이용

위의 소스에서 문제부분을 아래처럼 바꿔주자!

```python
#module_demo/util.py

####여기서 문제 발생 ####
import library
####################

from . import library

# main.py기준 실행시 잘돌아감
```

**but** util.py를 실행시킬경우 다른 에러가 발생

```python
Traceback (most recent call last):
  File "module_demo/util.py", line 11, in <module>
    from . import library
ImportError: attempted relative import with no known parent package
```

### 2-1. sys.path에 `module_demo`디렉터리 추가해 import시 module_demo를 찾게 만들기

```python
import sys
import os

### 경로 추가 ###
module_demo_path = os.path.join(os.getcwd(), 'module_demo')
sys.path.append(module_demo_path)
###############**

print('sys.path from main.py')
print('\n'.join(sys.path))
print()

print('__name__ of main.py')
print(__name__)
print()

from module_demo import library # 이제 그냥 import libray도 가능
from module_demo import util # 이제 그냥 import util도 가능
```

### 2-2. PYTHONPATH 환경 변수를 이용하기

2-1내용 지우고 그냥 바로 아래처럼 해주고 실행하면 됨!

```python
import sys
import os

# module_demo_path = os.path.join(os.getcwd(), 'module_demo')
# sys.path.append(module_demo_path)

print('sys.path from main.py')
print('\n'.join(sys.path))
print()

print('__name__ of main.py')
print(__name__)
print()
```

> ➜   export PYTHONPATH=/Users/Workspace/pydev/module_demo <br>
> ➜   python3 main.py
