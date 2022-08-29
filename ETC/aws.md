# AWS 1. IAM / EC2 / ELB / ElasticBeanstalk

## 1. IAM
각 개발자의 롤에 맞춰 적절한 접근제어가 필요한데, 이때 IAM을 사용함.
역할(role), 정책(policy)를 올바르게 구성해 IAM사용자와 연결
- 관리형 정책(Managed Policy) : 여러 정책을 그룹으로 묶어 사용. 재사용하기 좋음
- 인라인 정책(Inline Policy) : 재사용을 고려하지 않고 원하는 정책을 그때그때 연결

## 2. EC2(Elastic Compute Cloud)
vm 기반의 컴퓨팅 서비스로 메모리와 cpu가 인스턴스크기와 인스턴스 패밀리에 영향을 받는다.

<인스턴스의 수명주기>
![수명주기](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcrLWuI%2FbtqWn2N7gkU%2FyUzAwp76ljqwqmEBjXFb0K%2Fimg.png)
- AMI(Amazon Machine Image) : 기본 운영체제 이미지 
- 인스턴스 유형  : 애플리케이션 실행을 위한 가상 서버, CPU/메모리/스토리지 및 네트워킹 용량의 조합
- 인스턴스 세부정보 
  1. vpc : 리전마다 기본 vpc 및 서브넷이 설정되어 있음
  2. Public IP 자동 할당
- 보안그룹 : 임대한 인스턴스의 가상 방화벽으로 인바운드/아웃바운드 규칙을 설정할 수 있음
  1.  인바운드 : EC2인스턴스로 들어오는 트래픽에 대한 규칙. 특정 프로토콜, 포트의 접근을 허용하고 이외는 들어오지 못하게 처리(화이트리스트 방식)
  2. 아웃바운드 : 인스턴스에서 내보낼때, 해당 트래픽에 대한 규칙. default는 모든트래픽 허용한다.

### 오토스케일링
서버의 과부하, 장애 등과 같이 서비스 불능 상황 발생시 자동으로 서버를 복제하여 **서버 대수를 늘려주는 작업**을 해주는 AWS 서비스<br>
하나의 서버를 확장하는 스케일업(scale up)이 아닌 여러 서버로 서버수가 늘어나는 스케일 아웃(scale out)방식이다.

> #### 온프로미스?
> 클라우드환경과 대조되는 개념으로, 기업이 물리적 서버를 직접 구축해 사용하는 형태를 의미
> <br> 단점: 장비유지보수 비용이 비싸며, 서버 증설의 까다로움이 있음


## 3. ELB(Elastic Load Balancing)
하나의 서버에 많은 트래픽이 몰릴경우 부하가 몰리지 않게 적절히 분산해주는 작업을 해준다.<br>
4가지 종류가 있으며 모두 고가용성, 자동조정, 강력한 보안 나아가 상태 체크 기능을 제공해준다

## 4. EB(Elastic Beanstalk)
> EC2 + Auto Scaling + ELB 통합기능을 제공

사용자의 요구에 맞게 시스템 자원을 할당, 배치, 배포해 두었다 필요시 즉시 사용할 수 있는 상태로 미리 준히바는 프로비저닝 기능을 제공<br>

#### <사용순서>
![사용순서](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcbHlIV%2FbtqVZS1t5ex%2FXwTFhBQbtrQejjQJ2dODxK%2Fimg.png)

어플리케이션을 생성 -> 어플리케이션 소스 번들의 형태로 어플리케이션 버전을 ElasticBeanstalk에 업로드<br> -> EB가 자동으로 환경을 실행하고 필요한 aws리소스를 생성 및 구성함 -> 환경 실행 후에는 직접 환경을 관리하고 새로운 앱 버전을 배포 할 수 있음
