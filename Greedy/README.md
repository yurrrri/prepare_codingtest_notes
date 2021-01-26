### **그리디(Greedy) 알고리즘이란?**

greedy : 탐욕스러운 -> 탐욕법으로 부르기도한다.

그때그때 좋은것만 고르는 방법

따라서 '**가장**' 이라는 말과 자주 등장하며, '가장' 이라는 말은 정렬 알고리즘과 어울리므로  **정렬과 자주 엮인다.**

**[예제 3-1) 거스름돈](https://github.com/yurrrri/python_algorithm/blob/main/Greedy/greedy_moneychange.py)**

1260원을 거슬러줄 때 최소 동전의 개수 -> 금액이 큰 화폐부터 나누며 더해나감

```
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
