# 프로세스 & 스레드

## 프로세스(process)

- 컴퓨터에서 연속적으로 실행되고 있는 컴퓨터 프로그램 ⇒ 메모리에 올라와 실행되고 있는 프로그램의 독립적인 개체(인스턴스)
- 운영체제로 부터 시스템 **자원을 할당받는 작업의 단위**이다<br>
→ 할당받는 시스템 자원의 예시) cpu시간 /  운영되기 위해 필요한 주소&공간 / code, data, stack, heap의 구조로 되어있는 독립된 메모리 영역
- 특징
    
    ![https://gmlwjd9405.github.io/images/os-process-and-thread/process.png](https://gmlwjd9405.github.io/images/os-process-and-thread/process.png)
    
    프로세스는 각각 독립된 메모리 영역(위그림처럼 code, data, stack, heap구조로 이루어짐)을 할당받음.
    
    프로세스당 **최소 1개의 (메인)스레드**를 가지고 있음
    
    프로세스끼리는 별도의 주소공간에서 실행되며, 서로 접근할 수 없음 ⇒ 접근하고 싶다면 프로레스간의 통신을 사용해야함(ex. 파이프, 파일, 소켓등을 이용한 통신방법 이용)
    

### 프로세스의 구조

![https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FAjqpy%2FbtrgGrgTjp3%2FxrlTPkHIXEnt6lEF5p2Gt1%2Fimg.png](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FAjqpy%2FbtrgGrgTjp3%2FxrlTPkHIXEnt6lEF5p2Gt1%2Fimg.png)

> code(컴파일된 코드) - data(변수, 초기화된 데이터) - stack(임시데이터(함수호출, 로컬변수등) 저장) - heap(코드에서 동적으로 만들어지는 데이터 저장)

위와 같은 식으로 프로세스가 구성되고 이를 CPU가 읽으며 실행한다. 

## 스레드(Thread)

- 프로세스 내에서 실행되는 여러 흐름의 단위 → 프로레스가 할당받은 자원을 이용하는 실행의 단위임
- 프로세스의 특정한 수행경로로, 프로세스가 할당받은 **자원을 이용하는 실행의 단위**이다
- 특징
    
    ![https://gmlwjd9405.github.io/images/os-process-and-thread/thread.png](https://gmlwjd9405.github.io/images/os-process-and-thread/thread.png)
    
    스레드는 프로세스 내에서 각각 stack만 따로 할당받음(code, data, heap은 공유됨)
    
    한 프로세스내 여러 스레드끼리 주소공간이나, 자원등을 공유하면서 실행된다
    
    각각의 스레드는 별도의 레지스터와 스택을 가지고 있는데, 힙메모리는 서로 읽고 쓸 수 있음
    
    하나의 스레드가 프로세스 자원 변경시, 다른 이웃 스레드도 그 변경 결과를 즉시 볼 수 있다.
    

## 멀티 프로레스 vs 멀티 스레드

![https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FbQK2ht%2FbtrgC6LxZ2H%2F9pPh5WgFTLpRZ9bgPKdoq0%2Fimg.png](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FbQK2ht%2FbtrgC6LxZ2H%2F9pPh5WgFTLpRZ9bgPKdoq0%2Fimg.png)

 

![https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FPyQZ4%2FbtrgDdjcBFu%2Fj2kt3wfwT3KPCPlBCjdi4k%2Fimg.png](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FPyQZ4%2FbtrgDdjcBFu%2Fj2kt3wfwT3KPCPlBCjdi4k%2Fimg.png)

### 멀티 프로세스

하나의 응용프로그램을 여러개의 프로세스(CPU)로 구성해서 각 프로세스가 하나의 작업을 동시에 처리하도록 하는것(병렬처리)

- 장점 : 여러 자식프로세스중 문제 발생시 그 자식 프로세스만 죽는것 이상으로 영향이 확산되지 않음
- 단점
    - 프로세스사이는 각각 독립된 메모리 영역을 할당 받았는데, 프로세스들 사이 통신을 위해 복잡한 통신과정이 필요하다
    - context switching에서의 오버해드
        
        context switching 과정에서 무거운 작업이 진행되고 많은 시간이 소모되는등의 문제가 발생
        
        프로세스 사이의 공유 메모리가 없는데 context switching발생시 캐쉬정보 다 리셋후 다시 정보를 받아야함
        
        →context switching : cpu내에서 여러 프로세스를 돌아가며 작업을 처리하는데 이 과정을 말함.
        

### 멀티 스레드

![https://user-images.githubusercontent.com/48986787/126673676-992e01be-01a1-41cc-9a07-f5d6c2f2bba4.png](https://user-images.githubusercontent.com/48986787/126673676-992e01be-01a1-41cc-9a07-f5d6c2f2bba4.png)

하나의 응용프로그램을 여러개의 스레드로 구성해서 각 스레드로 하여금 하나의 작업을 처리하게 함, 많은 운영체제들이 멀티 프로세싱을 지원하는데 멀티 스레딩을 기본으로 하고있음. **웹서버**가 대표적인 멀티 스레드 응용프로그램임 

- 장점
    - 시스템 자원소모 감소(자원의 효율성 증대) : 프로세스를 생성해서 자원을 할당하는 시스템 콜이 줄어 자원을 효율적으로 관리할 수 있음
    - 시스템 처리량 증가(처리비용감소) : 스레드간 데이터 주고받는게 간단해져 시스템 자원소모가 줄어듬, 스레드 사이의 작업량이 줄어 context switching이 빠름
    - 간단한 통신방법으로 인한 프로그램 응답 시간 단축 : 프로세스내 stack영역 제외한 모든걸 공유하기때문에 통신의 부담이 적음
- 단점
    - 디버깅 까다로움 + 주의 깊은 설계가 필요
    - 하나의 스레드 문제 발생시 전체 프로세스 영향 받음
    (멀티프로세스는 하나 문제생겨도 다른 프로세스 실행에는 영향이 가지않는다)
    - 여러 스레드가 동일한 자원에 접근하기 때문에 동기화 이슈가 발생 할수도 있다

### 멀티 프로세스 대신 멀티 스레드를 사용하는 이유?

여러개의프로그램을 켜는대신 하나의 프로그램에서 여러 일을 시키는게 왜 좋을까?

- 이경우 프로세스 생성해서 자원할당하는 과정(시스템콜)이 줄어든다
- 스레드의 경우 프로세스내의 메모리 공유가 되기때문에 스레드간 데이터 교환이 간단해짐 + 통신도 부담줌
- 프로세스 전환속도 보다 스레드 전환속도가 빠름

⇒ 단 스레딩의 경우 동기화문제 + 동일 스레드내에서는 전역변수이용시 함께 이용하게되면 충돌이 발생할 수 있음
