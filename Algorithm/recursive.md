# 재귀함수(Recursive Fuction)

## 재귀함수의 정의

> 자기 자신을 다시 호출하는 함수!

재귀함수를 문제 풀이에서 사용할 때는 재귀 함수가 언제 끝날지, 종료조건을 꼭 명시해야한다. 명시하지 않을 경우 무한루프에 빠진다

```python
def recursive_fuction(i):
	#10번째 출력시 종료되도록 명시
	if i == 10:
		return
	print(i, '번째 함수에서', i + 1, '번째 재귀 함수를 호출합니다')
	recursive_fuction(i + 1)
	print(i, '번째 재귀함수를 종료합니다.')

recursive_fuction(1)
```

재귀함수는 `스택자료구조`를 이용한다. <br>
함수를 계속 호출시 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료 되기 때문. 

스택자료구조를 활용하는 상당수의 알고리즘은 재귀함수를 이용해서 간편하게 구현할 수 있다 

ex)DFS

## 재귀함수의 예시

### 1. Factorial 문제

n이 1 이하가 되었을때 함수를 종료하는 재귀함수형태로 구현 가능

```python
#반복적으로 구현한 n!
def factorial_iterative(n):
	result = 1
	#1부터 n까지의 수를 곱하기
	for i in range(1, n+1):
		result *= i
	return result

#재귀함수로 구현한 n!
def factorial_recursive(n):
	if n <= 1: #1이하인 경우 1을 반환
		return 1	
			#n! = n * (n-1)!를 그대로 코드로 작성하기
	return n * (n-1)
```

재귀함수나 반복적으로 구현한 함수나 결과는 동일. 
> 재귀함수의 장점 : 더 간결하다.

### 2. 구구단
```python
def multi_table(n):
	if n==0:
		print("end")
	else:
		multi_talbe(n-1)
		print("2 * {} = {}".format(n, 2*(n)))

multi_table(10)
	
```

### 3. 최대공약수(유클리드 호제법)
유클리드 호제법 : 두개의 자연수에 대한 `최대 공약수`를 구하는 대표적인 알고리즘

![유클리드 호제법](https://velog.velcdn.com/images%2Fjewon119%2Fpost%2F2a8ba029-20b9-477e-993f-b80c8be732f1%2Fsdf.png)

```python
def gcd(a,b):
	if a % b == 0:
		return b
	else:
		return gcd(b, a%b)

print(gcd(192, 162))

# 결과는 6
```