# SW Expert Academy [모의 SW 역량테스트] 

### 1952. 수영장

```python
def swim(n, price, d, m, m3):
    global minPrice
    if n > 12:
        if minPrice > price:
            minPrice = price
    elif price >= minPrice: # 이미 최소비용이 넘어갔기에 제외! (가지치기)
        return
    else:
        swim(n + 1, price + min(d*plan[n], m), d, m, m3) # n월 1일권과 1달권 비교
        swim(n + 3, price + m3, d, m, m3) # n월 3달 이용권

for t in range(1, int(input())+1):
    d, m, m3, y = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    minPrice = y
    swim(1, 0, d, m, m3)
    print('#{} {}'.format(t, minPrice))
```

### 4008. 숫자 만들기

- 음수에 대한 나눗셈 _ python 기준

  ```python
  a, b = -3, 2
  print(a//b) # -2
  print(int(a/b)) # -1, 현재 문제에서 사용할 경우
  if a < 0:
      print(-(abs(a)//b)) # -1
  else:
      print(a//b)
  ```

- 최대 최소 0으로 초기화하는 버릇 X

  문제에서 주어진 범위를 기준으로 초기화시켜주기

  ex) minV = 1000000, maxV = -10000000

```python
def cal(n, N, V, op1, op2, op3, op4):
    global minV, maxV
    if n == N:
        if V < minV:
            minV = V
        if V > maxV: # elif 사용하면 X
            maxV = V
    else:
        if op1 > 0:
            cal(n+1, N, V+nums[n], op1-1, op2, op3, op4)
        if op2 > 0:
            cal(n+1, N, V-nums[n], op1, op2-1, op3, op4)
        if op3 > 0:
            cal(n+1, N, V*nums[n], op1, op2, op3-1, op4)
        if op4 > 0:
            cal(n+1, N, int(V/nums[n]), op1, op2, op3, op4-1)

for t in range(1, int(input())+1):
    N = int(input())
    op1, op2, op3, op4 = map(int, input().split())
    nums = list(map(int, input().split()))
    minV = 100000000; maxV = -100000000
    cal(1, N, nums[0], op1, op2, op3, op4)
    print('#{} {}'.format(t, maxV-minV))
```

### 5658. 보물상자 비밀번호

```python
# sol1 : 16진수 직접 계산
for tc in range(int(input())):
    N, K = map(int, input().split())
    n = N//4
    nums = list(input())
    result = []
    for _ in range(n+1):
        for n1 in range(0, N, n):
            cal = 0
            cnt = 1
            for n2 in range(n1+n-1, n1-1, -1):
                if nums[n2] in 'ABCDEF': # A ~ F
                    cal += cnt * (ord(nums[n2]) - 55)
                else:
                    cal += cnt * int(nums[n2])
                cnt *= 16
                if n2 == n1 and cal not in result:
                    result.append(cal)
        nums.insert(0, nums.pop())

    result.sort(reverse=True)
    print('#{} {}'.format(tc+1, result[K-1]))
```

```python
# sol2 : int 성질 이용
# int('16진수', 16) = 10진수로!!

for tc in range(int(input())):
    N, K = map(int, input().split())
    n = N//4
    nums = list(input())
    result = []
    for _ in range(n+1):
        for n1 in range(0, N, n):
            cal = ''
            for n2 in range(n1, n1+n):
                cal += nums[n2]
            cal = int(cal, 16)
            if cal not in result:
                result.append(cal)
        nums.insert(0, nums.pop())

    result.sort(reverse=True)
    print('#{} {}'.format(tc+1, result[K-1]))
```

```python
# sol2-2 : int 성질 이용
for tc in range(int(input())):
    N, K = map(int, input().split())
    codes = list(map(str, input()))
    line = N//4
    numbers = []
    for i in range(line):
        for j in range(0, N, line):
            numlst = codes[j:j+line] # 한 변의 숫자들을 numlst에 저장하기
            num = int(''.join(numlst), 16) # 리스트를 16진수로 바꾸기
            if num not in numbers:
                numbers.append(num)
        codes.append(codes.pop(0))
    numbers.sort(reverse=True) # 내림차순으로 정리하기
    print('#{} {}'.format(tc+1, numbers[K-1]))
```

### 1953. [모의 SW 역량테스트\] 탈주범 검거



### 4012. [모의 SW 역량테스트\] 요리사

```python
def comb(lst, n): # lst에서 n개를 택하는 조합만들어 주는 함수
    ret = []
    if n > len(lst): return ret

    if n == 1:
        for i in lst:
            ret.append([i])
    elif n > 1:
        for i in range(len(lst) - n + 1):
            for temp in comb(lst[i + 1:], n - 1):
                ret.append([lst[i]] + temp)

    return ret


for tc in range(int(input())):
    N = int(input())
    Slst = [list(map(int, input().split())) for _ in range(N)]
    fresult = 9999999999
    R = N//2
    Alsts = comb([i for i in range(N)], R)
    for i in range(len(Alsts)):
        Alst = Alsts[i] # A에 들어갈 식재료 인덱스 저장
        Blst = []
        for j in range(N):
            if j not in Alst:
                Blst.append(j) # B에 A 외의 식재료 인덱스 저장
        result = 0

        # 식재료에서 2개를 택하는 조합 리스트를 저장한다.
        A = comb(Alst, 2)
        B = comb(Blst, 2)
        for k in range(len(A)):
            # 시너지 합의 차이를 더해준다.
            result += Slst[A[k][0]][A[k][1]] + Slst[A[k][1]][A[k][0]] - Slst[B[k][0]][B[k][1]] - Slst[B[k][1]][B[k][0]]
        # 맛의 차이가 최소인 경우를 구하기 위해 if문을 이용한다.
        if fresult > abs(result):
            fresult = abs(result)
    print('#{} {}'.format(tc+1, fresult))
```

### 5656. [모의 SW 역량테스트\] 벽돌 깨기

### 1949. [모의 SW 역량테스트\] 등산로 조성  