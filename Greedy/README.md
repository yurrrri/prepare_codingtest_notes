
### **그리디(Greedy) 알고리즘이란?**

greedy : 탐욕스러운 -> 탐욕법으로 부르기도한다.

그때그때 좋은것만 고르는 방법

따라서 '**가장**' 이라는 말과 자주 등장하며, '가장' 이라는 말은 정렬 알고리즘과 어울리므로  **정렬과 자주 엮인다.**

**[예제 1) 거스름돈](https://github.com/yurrrri/python_algorithm/blob/main/Greedy/greedy_1.py)**

1260원을 거슬러줄 때 최소 동전의 개수 -> 금액이 큰 화폐부터 나누며 더해나감

```python
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인하기
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)
```

**시간복잡도 : 화폐가 K개일때 O(K)**

**[예제 2) 큰 수의 법칙](https://github.com/yurrrri/python_algorithm/blob/main/Greedy/greedy_2.py)**

다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다. 단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다는 것이 이 법칙의 특징이다.

**입력 조건**
 - 첫째 줄에 N(2<=N<=1000), M(1<=M<=10000), K(1<=K<=10000)의 자연수가 주어지며, 
 - 각 자연수는 공백으로 구분한다. 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는
   1 이상 10,000 이하의 수로 주어진다.
  - 입력으로 주어지는 K는 항상 M보다 작거나 같다.

**출력 조건**

- 첫째 줄에 큰 수의 법칙에 따라 더해진 답을 출력한다.

**입력 / 출력 예시**
[예시 1]
5 8 3
2 4 5 4 6

46

[예시 2]
5 7 2
3 4 3 4 3

28

**[ 내 코드 ]**
```python
N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

# 오름차순정렬
nums.sort()

# 합
sum = 0
# 큰수
max = nums[-1]
# 두번째로 큰수
second_max = nums[-2]

while True:
    # 큰수부터 K번씩 더한뒤
    for _ in range(K):
        if M == 0:
            break
            sum += max
            M = M - 1
    if (M == 0):
        break
    #두번째로 큰 수를 더해주고, 다시 반복문 처음으로 돌아가 K번씩 더함
    sum += second_max
    M = M - 1

print(sum)
```

**[ 책 코드 ]**
```python
# N, M, K를 공백을 기준으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백을 기준으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort() # 입력 받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result) # 최종 답안 출력
```
