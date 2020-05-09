# Programming Advanced

### 시작하기

#### 5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수

- `int`, `format` 을 이용하여 문제 풀기

```python
for tc in range(int(input())):
    N, num = map(str, input().split())
    num_16 = int(num,16) # 16진수로 바꾸기
    num_2 = format(num_16,'b') # 2진수로 바꾸기
    while len(num_2) < int(N)*4: # 문제에 제시된 길이 맞춰주기
        num_2 = '0'+num_2
    print('#{} {}'.format(tc + 1, num_2))
```

- 아스키코드 이용하여 문제 풀기

```python
for tc in range(int(input())):
    N, num_16 = map(str, input().split())
    num_10 = 0
    cnt = 1
    # 16진수를 10진수로 바꾸기
    for i in num_16[::-1]:
        if ord('A') <= ord(i) <= ord('Z'):
            num_10 += cnt*(ord(i)-ord('A')+10)
        else:
            num_10 += cnt * int(i)
        cnt *= 16
    # 10진수를 2진수로 바꾸기
    num_2 = ''
    while num_10 != 0:
        num_2 += str(num_10 % 2)
        num_10 = num_10//2
    num_2 = str(num_2[::-1])
    # 자리수 문제에 제시된 대로 만들기
    while len(num_2) < int(N)*4:
        num_2 = '0'+num_2
    print('#{} {}'.format(tc + 1, num_2))
```

- 파이썬 라이브러리 최대로 활용하여 문제 풀기

```python
for tc in range(int(input())):
    N, S = input().split()
    N = int(N)
    print('#{}'.format(tc+1), end=' ')
    t = bin(int(S, 16))
    t = t[2:]
    if len(t) < N * 4:
        t = '0'*(N*4-len(t)) + t
    print(t)
```

- dictionary 이용하여 문제 풀기

```python
hex_number = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

def GetResult(n, str_num):
    ret = ''
    for i in range(n):
        number = hex_number[str_num[i]]
        tmp_ret = ''
        for j in range(3, -1, -1):
            bit = str((number >> j) & 1)
            tmp_ret += bit
        ret += tmp_ret
    return ret


for tc in range(int(input())):
    N, input_number = map(str, input().split())
    N = int(N)
    print('#{} {}'.format(tc+1, GetResult(N, input_number)))
```

#### 5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2 

```python
for tc in range(int(input())):
    N = float(input())
    result = ''
    a = 0.5
    while N != 0:
        # overflow 조건
        if len(result) >= 13:
            result = 'overflow'
            break
        # 2진수 계산하기
        else:
            if N >= a: # 1이 추가되는 경우
                result = result + '1'
                N -= a
            else: # 0이 추가되는 경우
                result = result + '0'
            a *= 0.5
    print('#{} {}'.format(tc+1, result))
```

### 완전 검색

#### 5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합

```python
# solution 1
def search(x, y, sum):
    global minV
    sum += board[x][y]
    if sum >= minV: # 가지치기
        return
    if x == N-1 and y == N-1: # 오른족 아래 끝까지 이동했을 경우 종료
        if minV > sum:
            minV = sum
        return
    else:
        dir = [[0, 1], [1, 0]]
        for i in range(2): 
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            if nx <= N-1 and ny <= N-1:
                search(nx, ny, sum)


for tc in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    minV = 999999999
    search(0, 0, 0) # x, y, sum
    print('#{} {}'.format(tc+1, minV))
```

```python
# solution 2 (더 간단하게 코드 작성)
def search(x, y, sum):
    global minV
    if sum >= minV:
        return # 이동 중단하고 다른 경로 탐색
    if x == N-1 and y == N-1: # 목적지 도착
        if minV > sum + board[x][y]:
            minV = sum + board[x][y]
    else:
        if x + 1 < N:
            search(x+1, y, sum + board[x][y])

        if y + 1 < N:
                search(x, y+1, sum + board[x][y])


for tc in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    minV = 999999999
    search(0, 0, 0) # x, y, sum
    print('#{} {}'.format(tc+1, minV))
```

![image-20200507120746728](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200507120746728.png)백트래킹

![image-20200507121020469](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200507121020469.png)

#### 5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트

```python
def perm(k, N):
    global minV
    if k == N:
        # 원하는 작업 수행
        sum = lst[0][arr[0]]
        for n in range(N):
            if n != N-1:
                sum += lst[arr[n]][arr[n+1]]
            else:
                sum += lst[arr[n]][0]
        if minV > sum:
            minV = sum
    # 순열만들기
    else:
        for i in range(k, N): # k 번째 원소를 i 번째 원소와 교환하여 저장
            arr[k], arr[i] = arr[i], arr[k]
            perm(k + 1, N)
            arr[k], arr[i] = arr[i], arr[k] # 리턴 후 i 번째 원소가 배제되지 않게 복구


for tc in range(int(input())):
    N = int(input())
    arr = [x for x in range(1, N)]
    lst = [list(map(int, input().split())) for _ in range(N)]
    minV = 9999999
    perm(0, N-1)
    print('#{} {}'.format(tc+1, minV))
```

![image-20200507121551451](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200507121551451.png)

### 탐욕 알고리즘

#### 5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반

```python
for tc in range(int(input())):
    N, M = map(int, input().split())
    Nw = list(map(int, input().split()))
    Mt = list(map(int, input().split()))
    amount = 0
    Nw.sort(reverse=True) # 값이 큰 순서로 정렬하기
    Mt.sort(reverse=True) # 값이 큰 순서로 정렬하기
    i = 0
    while len(Nw):
        if i >= len(Mt): # i : Mt에서 비교할 값 index의미
            break
        if Mt[i] >= max(Nw): # Mt의 값과 Nw의 양 비교하여 적재가능한지 체크하기            amount += max(Nw)
            amount += max(Nw) # 적재 가능하기에 amount에 추가하기
            Nw.pop(Nw.index(max(Nw))) # 적재된 화물 빼주기
            i += 1
        else:
            Nw.pop(0) # 적재할 트럭이 없기에 싣지 못하는 경우
    print('#{} {}'.format(tc+1, amount))
```

#### 5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크

```python
for tc in range(int(input())):
    N = int(input()) # 신청서 개수
    Nlst = []
    for n in range(N):
        Nlst.append(list(map(int, input().split())))
    ans = 1 # 1로 초기화된 이유는 처음에 신청 하나를 받는다고 가정 후에 코드가 작성되어 있기 때문이다.
    Nlst.sort(key=lambda x:x[1]) # 끝나는 시간 기준으로 정렬하기 위해 lambda 사용
    i = 0 # e 종료시간 찾아줄 index
    j = 1 # s 시작시간 찾아줄 index (e와 비교하기 위해 다른 변수 사용)
    while j < len(Nlst):
        now_e = Nlst[i][1]
        next_s = Nlst[j][0]
        if next_s >= now_e: # 다음 작업 가능한지 확인
            ans += 1
            i = j
            j += 1
        else: # 다음 작업 시작시간보다 종료시간이 길기에 다다음 작업 시작시간을 비교하기 위해 +1
            j += 1
    print('#{} {}'.format(tc+1, ans))
```

![image-20200507104114576](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200507104114576.png)

#### 5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임

```python
def check(lst, who): # baby-gin인지 확인하는 함수
    global winner
    for i in range(10):
        if lst[i] == 3: # triplet 인지 확인
            winner = who
            break
        elif i <= 7 and lst[i] > 0 and lst[i+1] > 0 and lst[i+2] >0: # run 인지 확인
            winner = who
            break


for tc in range(int(input())):
    cards = list(map(int, input().split()))
    player_1 = [0] * 10
    player_2 = [0] * 10
    winner = 0
    for i in range(0, 12, 2):
        player_1[cards[i]] += 1
        player_2[cards[i+1]] += 1
        if i >= 4: # 3장을 받았을 때 부터 확인 가능하기에 가지치기!!
            check(player_1, 1)
            if winner > 0: # 놓치기 쉬운 부분!! 
                # 순서대로 카드를 주기에 player_1이 baby-gin 이면 바로 종료
                break
            check(player_2, 2)
        if winner > 0:
            break
    print('#{} {}'.format(tc+1, winner))
```

### 분할 정복

### 백트래킹

### 그래프의 기본과 탐색

### 그래프의 최소 비용 문제

### 문자열 탐색

### 동적 계획법의 소개

### 동적 계획법의 적용

### 동적 계획법의 활용

### NP-Complete

### 근사 알고리즘