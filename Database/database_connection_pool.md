# DataBase Connection Pool, DBCP(데이터베이스 풀)

> 회사에서 개발자분들과 이야기하던중 데이터베이스풀이라는 개념이 나와 정리해보았다<br>
> 구글링해보니 자바에서 많이 쓰이는 개념인것으로 확인.<br>
> 파이썬의 경우도 구현된 블로그들이 있어 참고해 추가 할 예정!

## Database Connection Pool의 정의
<img src="https://assets.digitalocean.com/articles/managed_db_pools/with_connection_pool.png">

애플리케이션의 스레드에서 데이터베이스에 접근하기위해 Connection이 생성되는데. <br>
이때 일정 수준 이상의 사용자 요청이 들어와 Connection이 생성된다면 서버에 과부하가 걸리게된다<br>
> 데이터베이스와 Connection한 객체들을 미리 생성해 **Pool**에 저장해두었다가, 클라이언트의 요청이 들어올 때마다 사용/반환하는 방식

connection pool에서 Connection 정보를 관리하기 때문에 DB에 연결하기 위한 연결 정보 생성 시간이 없어 DB Connection 위한 시간이 월등히 줄어든다. 

### Connection이 부족할 경우

- 모든 Connection이 요청을 처리 중일 때, 해당 클라이언트의 요청을 대기 상태로 전환한다
- 이후 Pool에 Connection 객체가 반환되면 순차적으로 요청을 처리

## Connection Pool의 과정
### ー만약 Connection Pool이 없다면?(자바예시)
1. DB 서버 접속정보를 위해 JDBC드라이버를 로드한다
2. DB 접속 정보와 특정 메소드를 통해 DB Connection객체를 얻는다
3. Connetion 객체로 부터 쿼리를 수행하기 위한 객체를 받는다
4. 쿼리를 수행해 그 결과로 result 객체를 받아 데이터를 처리한다
5. 처리가 완료되면 처리에 사용된 리소스를 close해 반환한다

### ーConnection Pool을 쓰면?
1. 웹이 실행되면 데이터베이스와 연결된 Connection 객체들을 미리 생성해 Pool에 저장해 둔다
2. 클라이언트 요청 시 Pool에서 Connection 객체를 가져와 사용한다
3. 클라이언트가 요청한 처리가 끝나면 사용된 Connection 객체를 다시 Pool에 반환한다

# Connection Pool의 속성값
- maxActive : 동시에 사용할 수 있는 최대 커넥션 개수
- maxIdle : Connection Pool에 반납될 때 최대로 유지될 수 있는 커넥션의 개수
- minIdle : 최소한으로 유지할 커넥션 개수
- initialSize : 최초로 커넥션매서드를 통해 커넥션 풀에 채워 넣을 커넥션 개수

* maxActive >= initialSize (최대 커넥션 수는 초기 생성 커넥션 수보다 크거나 같게 설정되어야 한다)
* maxActive = maxIdle (같은것이 바람직하다)

## Connection Pool의 장점 

- 매 연결마다 Connection 객체를 생성/제거하는 비용 감소

- 미리 생성된 Connection 객체를 사용해 데이터베이스 접근 시간 단축

- Connection 갯수를 제한해 부하 조정

- Database 접속 모듈을 공통화해 Database 서버의 환경이 바뀌어도 유지보수가 쉬움


## Connection Pool의 단점

- Connection 또한 객체이므로 메모리 차지

- Connection 개수를 잘못 설정할 경우, 쓸모없는 Connection이 발생할 수 있음

> Thread Pool과 Connection Pool
> - 애플리케이션의 `Thread Pool`과 Connection Pool의 `Connection의 수`는 메모리와 **직접적으로 관련이 있음**
> - Connection과 Thread 수를 많이 설정하면 메모리를 많이 차지하고, 반대로 적게 설정할 경우 처리하지 못하는 대기 요청이 많아짐
