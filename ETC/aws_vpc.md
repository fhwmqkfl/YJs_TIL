# VPC(Virtual Private Cloud)
> Amazon Virtual Private Cloud(Amazon VPC)를 이용하면 사용자가 정의한 가상 네트워크로 AWS 리소스를 시작할 수 있습니다. 이 가상 네트워크는 AWS의 확장 가능한 인프라를 사용한다는 이점과 함께 고객의 자체 데이터 센터에서 운영하는 기존 네트워크와 매우 유사합니다. _출처 : aws 공식 홈페이지_

## Intro
VPC가 없는 경우 아래의 이미지처럼 모든 인스턴스들이 복잡하게 얽히게 된다 -> 이런 구조는 시스템을 복잡하고 어렵게 만든다
<img src="https://miro.medium.com/max/1400/1*hZGJeN-4F6fLtus5XBJC_w.png">

## VPC
AWS Cloud 내부에서 구성되는 사용자의 AWS 계정 전용 가상 네트워크
<img src="https://miro.medium.com/max/1400/1*Ehn4uEQMtbmdPsU6MxVc3Q.png">
위의 이미지 처럼 VPC를 적용하면 VPC별로 네트워크 구성및 설정이 가능해짐.<br>
각각의 VPC는 완전 독립된 네트워크처럼 작동한다<br>
여기서 주의할 점은 각 VPC는 하나의 리전에 종속된다. 

## VPC의 구축
<img src="https://miro.medium.com/max/1400/1*Bjb_sU3iu7_Z9Djeh3Zwdw.png">
VPC 구축을 위해 아이피 범위를 RFC1918이라는 사설아이피 대역에 맞춰 구축되어야 한다.

> **VPC에서 사용되는 IP대역**

* 10.0.0.0 - 10.255.255.255 (10/8 prefix)
* 172.16.0.0 - 172.31.255.255 (172.16/12 prefix)
* 192.168.0.0 - 192.168.255.255 (192.168/16 prefix)

한 리전안에 VPC를 여러개 생성할때 서로 아이피는 겹치면 안됨!(생성은 되지만 DNS IP를 잡지 못하는 에러가 발생)
> 예를 들어, 기본 VPC가 `172.31.0.0/16`으로 생성되어 있다면 우리는 _172.31_ 네트워크 IP주소를 피해서 생성해야 한다.


### 서브넷
<img src="https://miro.medium.com/max/1400/1*WCucO_PRVCShRY2Swe1HGQ.png">

> 서브넷 : VPC의 IP 주소를 나누어 리소스가 배치되는 물리적인 주소 범위를 뜻한다.

VPC가 논리적인 범위를 의미한다면, 서브넷은 VPC안에서 실제로 리소스가 생성될 수 있는 네트워크 영역(EC2, RDS같은 리소스를 생성 할 수 있음)

다만 VPC가 하나의 리전에 생성이 가능하듯이 서브넷은 하나의 AZ(가용영역)에서만 생성이 가능하다!

> public subnet / private subnet <br>
인터넷과 연결되어 있는 서브넷을 public subnet이라 하고, 인터넷과 연결되어있지 않은 서브넷을 private subnet이라고 함


### 라우팅 테이블과 라우터
<img src="https://miro.medium.com/max/1400/1*C_j93s0KB4JwfLgck5YFug.png">

네트워크 요청이 발생하게 되면 데이터는 라우터로 가게된다.<br>
VPC안의 네트워크 범위를 갖는 네트워크 요청은 로컬에서 찾도록 되어있는데, 그 외의 외부로 통화는 트래픽은 처리할수 없다 -> 이때 **인터넷 게이트웨이**를 사용한다.<br>
> VPC내부의 모든 서브넷에 대해서는 디폴트로 라우팅이 자동으로 생성되어 있다

### 인터넷게이트웨이
<img src="https://miro.medium.com/max/1400/1*I_3RxWyOPMj9lQs1xhEebg.png">

기본적으로 격리된 네트워크 환경인 VPC는 기본적으로 인터넷을 사용할 수 없다.<br>
인터넷 게이트웨이는 VPC리소스와 인터넷 간의 관문으로 앞에 설명한 `퍼블릭서브넷`의 경우 **인터넷 게이트웨이를 라우팅 테이블에 설정하고 등록**해줘야 한다.
