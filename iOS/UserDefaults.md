# UserDefaults

> 데이터를 영구적으로 저장하기위한 여러 수단중 하나.  앱의 전용공간에 plist형태로 저장됨
> 
- plist란?

    property list 의 줄임말<br>
    실행 패키지에 관한 필수 설정 정보가 포함된 구조화된 텍스트 파일로 키-벨류로 구성되어있음.
    시스템은 plist의 키-벨류를 이용해 앱,앱설정을 가져옴<br>
    
    XML형식이다
    

<aside>
💫 An interface to the user’s defaults database, where you store <b>key-value pairs</b> persistently across launches of your app.

Apps store these preferences by assigning values to a set of parameters in a user’s defaults database. The parameters are referred to as *defaults* because they’re commonly used to determine an app’s default state at startup or the way it acts by default.

</aside>

 **데이터 저장소**로 앱의 어느곳에서나 데이터를 쉽게 읽고 저장할 수 있음

사용자 기본 설정과 같은 단일 데이터 값에 적합 → 복잡할경우 별도의 DB, CoreData 사용 추천

스위프트 기본 타입 데이터는 대부분 그대로 저장이 가능하다고 함!

```swift
앱이 꺼져도 데이터는 유지되지만, 삭제된다? -> 다 사라짐^^

Local DB 이기 때문에 앱 내부에 저장되는데 -> 앱이 삭제되면 다 사라지기 때문
```

---

다양한 기능을 제공하고 있지만, 보통은 `.standard` 라는 싱글톤 객체를 이용해 저장, 읽기 정도의 단순한 메서드를 주로 사용한다고 함

## 설정 저장

```swift
// Key : age, Value 31 저장
var x = 31
UserDefaults.standard.set(x, forKey:"age")

x = 20

print(UserDefaults.standard.integer(forKey: "age")) // 31이나옴 -> x가 바뀌면 새로 저장해줘야함
```

## 설정 읽어오기

```swift
// 타입신경쓰기
let age = UserDefaults.standard.integer(forKey: "age")

// 캐스팅방식도 가능
let age = UserDefaults.standard.object(forKey: "age") as? Int
```

## 설정 삭제하기

```swift
UserDefaults.standard.removeObject(forKey: "age")
// 혹은 nil 설정
```

---

## 기본값 세팅하기

앱 시작시 항상 실행되게 작성해놔야함 ⇒ 메모리상에서만 저장되기때문

```swift
// register(defaults:)사용
UserDefaults.standard.register(
	defaults: [
		"key1": true,
		"key2": 10,
		"key3": "value"
	])
```

---

## 사용자 정의타입(구조체) 저장&읽기

1. 저장
    
    Data형으로 변경하는 작업(인코딩)을 해줘야함 → `Codable` , `JSONEncoder`이용
    
    ```swift
    /* 에러발생 */
    struct Human {
        let name: String
    }
    
    let human: Human = Human(name: "애플")
    UserDefaults.standard.set(Human, forKey: "Human") // ERROR!!
    
    /* 처리방법 */
    // 1. Codable 프로토콜 채택
    struct Human: Codable {
        let name: String
    }
    // 2. Data형 변경후 set호출
    let encoder: JSONEncoder = JSONEncoder()
    if let encoded = try? encoder.encode(human) {
        UserDefaults.standard.set(encoded, forKey: "Human")
    }
    ```
    
2. 읽기
    
    Data형에서 원래 타입(Human)으로 돌아오는 작업(디코딩)을 해줌 → `JSONDecoder`이용
    
    ```swift
    let decoder: JSONDecoder = JSONDecoder()
    if let data = UserDefaults.standard.object(forKey: "Human") as? Data,
       let human = try? decoder.decode(Human.self, from: data) {
    }
    ```
    

## JSON을 이용한 복잡한 데이터 저장&읽기 → 가능

JSONEncoder를 활용한 인코딩방식 이용