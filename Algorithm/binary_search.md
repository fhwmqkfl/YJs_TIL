# 이진 탐색(리스트 내에서 데이터를 매우 빠르게 탐색 하는 방법)

![이진 탐색](https://user-images.githubusercontent.com/71719160/188174421-d66f2edb-8266-4243-b903-679698cad227.png)

데이터가 정렬되어있는 배열에서 특정한 값을 찾아내는 알고리즘.
배열의 중간에 있는 임의의 값을 선택하여 찾고자 하는 값 X와 비교한다.

X가 중간 값보다 작으면 중간 값을 기준으로 좌측의 데이터들을 대상으로
X가 중간값보다 크면 배열의 우측을 대상으로
다시 탐색한다.

동일한 방법으로 다시 중간의 값을 임의로 선택하고 비교한다. (해당 값을 찾을 때까지 반복)

## preview : 순차탐색
리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법이다.<br>
보통 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용한다. <br>
시간만 충분하다면 아무리 데이터가 많아도 항상 원하는 데이터를 찾을 수 있다는 장점이 있다.<br>

```python
#순차 탐색 코트 구현
def sequential_search(n, target, array):
  #각 원소 하나씩 확인
	for i in range(n):
		#현재의 원소가 찾고자 하는 원소와 동일한 경우
		if array[i] == target:
			return i + 1 #현재의 위치 반환(인덱스는 0부터 시작하니까 1더하기)

#print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요")
input_data = input().split()
n = input_data[0]
target = input_data[1]

#print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

#순차 탐색 수행 결과 출력
print(sequential_search(n, target, array))
```

### 순차탐색의 시간복잡도
    
순차탐색은 데이터의 정렬여부와 관련없이 가장 앞에 있는 원소부터 하나씩 확인해야 한다는 점이 특징이다. <br>
따라서 데이터의 개수가 N개일 때 최대 N번의 비교연산이 필요하므로 순차탐색의 최악의 경우 `시간복잡도는 O(N)`이다
    
## 이진 탐색 : 반으로 쪼개면서 탐색하기

이진탐색(Binary Search)은 배열 내부의 데이터가 **정렬**되어있어야먄 사용할 수 있는 알고리즘이다(데이터가 무작위일 경우 사용❌)<br>
이진 탐색은 탐색 범위를 절반식 좁혀가며 데이터를 탐색하는 특성이 있다. 

이진탐색은 위치를 나타내는 변수 3개를 사용하는데, 탐색하고자 하는 범위의 **시작점** , **끝점** 그리고 **중간점**이 있다.<br>
찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는게 이진탐색 과정이다.<br>
이진탐색은 한번 확인할 때마다 절반씩 데이터를 줄어들도록 만드는데 이는 `퀵 정렬`과 동일하다

### 이진 탐색의 시간복잡도
이진탐색의 경우 한번 확인을 거칠 때마다 확인하는 원소가 평균적으로 절반으로 줄어든다. 
* 평균 : `O(logN)`
* 최선 : 정 가운데 있는 값이 내가 원하는 값일 경우, `O(1)`


### 이진 탐색 구현방법 1 : 재귀함수

```python
#재귀함수로 이진 탐색 소스코드 구현
def binary_search(array, target, start, end):
	if start > end:
		return None:
	mid = (start + end) // 2
	#찾은 경우 중간점 인덱스 반환
	if array[mid] == target:
		return mid
	#중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
	elif array[mid] > target:
		return binary_search(array, target, start, end - 1)
	#중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
	else:
		return binary_search(array, target, start, end - 1)

#n(원소의 개수)과 target(찾고자 하는 몬자열)을 입력받기
n, target = input().split()
#전체 원소 입력받기
array = list(map(int, input().split()))

#이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1):
if result == None:
	print("원소가 존재하지 않습니다.")
else:
	print(result + 1)
```

### 이진 탐색 구현방법 2 : 단순하게 반복문 이용

```python
#반복문으로 이진 탐색 소스코드 구현
def binary_search(array, target, start, end):
	while start <= end:
		mid = (start + end) // 2
		#찾은 경우 중간점 인덱스 반환
		if array[mid] == target:
			return mid
		#중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
		elif array[mid] < target:
			end = mid - 1
		#중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
		else:
			start = mid + 1
	return None

#n(원소의 개수)과 target(찾고자 하는 몬자열)을 입력받기
n, target = input().split()
#전체 원소 입력받기
array = list(map(int, input().split()))

#이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1):

if result == None:
	print("원소가 존재하지 않습니다.")
else:
	print(result + 1)
```
