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

#### 5207. [파이썬 S/W 문제해결 구현] 4일차 - 이진 탐색

```python
def binary_check(lst, num):
    global cnt
    l = 0
    r = N - 1
    check = -1 # 번갈아 탐색하는 지 확인하기 위한 변수 (오른쪽 구간: 1, 왼쪽 구간: 2)
    while l <= r:
        mid = (r + l)//2
        if num == lst[mid]:
            cnt += 1
            return
        elif num > lst[mid]: # 오른쪽 구간
            if check == 1:
                return
            l = mid + 1
            check = 1
        elif num < lst[mid]: # 왼쪽 구간
            if check == 2:
                return
            r = mid - 1
            check = 2


for tc in range(int(input())):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split())) # A에 있는지 확인할 숫자
    cnt = 0
    for b in range(M):
        binary_check(A, B[b])
    print('#{} {}'.format(tc+1, cnt))
```





### 백트래킹

#### 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용

```python
def backtrack(idx, price):
    global N, f_price
    if idx == N:
        if price < f_price:
            f_price = price
        return
    if price > f_price: # 가지치기
        return
    for i in range(N):
        if not col[i]: 
            col[i] = 1
            backtrack(idx+1, price + arr[i][idx])
            col[i] = 0

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    col = [0] * N
    f_price = 9999999 # [주의] 0으로 두면 안된다!!
    backtrack(0, 0)
    print('#{} {}'.format(tc+1, f_price))
```

```python
# 순열 이용

def backtrack(price, selected, idx, N):
    global f_price
    if idx == N:
        if price < f_price:
            f_price = price
        return
    # 사용가능한 선택지 후보군에 대하여 다음단계로 진행
    if price > f_price:
        return
    for i in range(N):
        if not selected[i]:
            selected[i] = 1
            backtrack(price + arr[idx][i], selected, idx + 1, N)
            selected[i] = 0

for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    col = [0] * N
    f_price = 9999999 # [주의] 0으로 두면 안된다!!
    backtrack(0, [0]*N, 0, N)
    print('#{} {}'.format(tc+1, f_price))
```

![image-20200521124421421](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200521124421421.png)

nqueen 처럼

### 5208. [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2

```python
def backtrack(idx, remain, cnt):
    global f_cnt, N
    remain -= 1 # 다음 정류장에 도착하면 배터리 감소
    if idx == N:
        if cnt < f_cnt:
            f_cnt = cnt
        return
    # 가지치기
    if cnt > f_cnt:
        return
    # 배터리를 교환하고 다음 정류장으로 진행
    backtrack(idx+1, stops[idx], cnt+1)
    # 배터리를 교환하지 않고 다음 정류장으로 진행
    if remain > 0:
        backtrack(idx+1, remain, cnt)


for tc in range(int(input())):
    stops = list(map(int, input().split()))
    N = stops[0] # 정류장의 개수
    f_cnt = 99999999
    backtrack(2, stops[1], 0)
    print('#{} {}'.format(tc+1, f_cnt))
```



### 그래프의 기본과 탐색

#### 5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기

```python
def make_set(x):
    p[x] = x


def find_set(x):
    if p[x] == x: return x
    else:
        p[x] = find_set(p[x])
        return p[x]


def union(x, y):
    px = find_set(y) # x의 대표자
    py = find_set(x) # y의 대표자
    if rank[px] > rank[py]:
        p[py] = px
    else:
        p[px] = py
        if rank[px] == rank[py]:
            rank[py] += 1


for tc in range(int(input())):
    N, M = map(int, input().split())
    Mlst = list(map(int, input().split()))
    p = [0] * (N+1)
    rank = [0] * (N + 1)
    for i in range(1, N+1):
        make_set(i)
    for j in range(M):
        union(Mlst[2*j],Mlst[2*j+1])

    result = []
    for i in range(len(p)):
        result.append(find_set(i))
    print('#{} {}'.format(tc+1,len(set(result)) - 1))
```

![image-20200522131014828](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200522131014828.png)

### 그래프의 최소 비용 문제

#### 5249. [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리

```python
import heapq

for tc in range(int(input())):
    V, E = map(int, input().split())
    adj = {i: [] for i in range(V+1)}  # 인접리스트
    for i in range(E):
        s, e, c = map(int, input().split())  # 시작정점, 끝정점, 가중치
        adj[s].append([e, c])
        adj[e].append([s, c])

    # key, mst, 우선순위 큐 준비
    INF = float('inf')
    key = [INF] * (V+1)
    mst = [False] * (V+1)
    pq = []

    # 시작점 선택 : 0번 선택
    key[0] = 0
    # 큐에 시작정점을 넣는다! (key, 정점인덱스)
    # 우선순위 큐 -> 이진힙 -> library : heapq
    heapq.heappush(pq, (0, 0))  # 우선순위 큐(원소의 첫번재 요소) : key를 우선순위로
    result = 0
    while pq:
        # 최소값 찾기
        k, node = heapq.heappop(pq)  # 가장 작은값 꺼낸다. (key, u)
        if mst[node]: continue  # old 한 정보면 스킵
        # mst로 선택
        mst[node] = True
        result += k
        # key 값을 갱신 => key 배열/큐
        for dest, wt in adj[node]:  # dest 가고자하는 곳, wt 가중치
            if not mst[dest] and key[dest] > wt:
                key[dest] = wt
                # 큐 갱신 => 새로운 (key, 정점) 삽입 (필요없는 원소는 스킵)
                heapq.heappush(pq, (key[dest], dest))

    print('#{} {}'.format(tc+1, result))
```

![image-20200522123304273](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200522123304273.png)

#### 5250. [파이썬 S/W 문제해결 구현] 7일차 - 최소 비용

```python

```

#### 5251. [파이썬 S/W 문제해결 구현] 7일차 - 최소 이동 거리

```python
for tc in range(int(input())):

    V, E = map(int, input().split())
    adj = {i: [] for i in range(V+1)}  # 인접리스트
    for i in range(E):
        s, e, c = map(int, input().split())
        adj[s].append([e, c])  # 단방향이기에

    INF = float('inf')
    dist = [INF] * (V+1)
    selected = [False] * (V+1)

    dist[0] = 0
    cnt = 0
    while cnt < V+1:
        # dist 가 최소인 정점 찾기
        min = INF
        u = -1
        for i in range(V+1):
            if not selected[i] and dist[i] < min:
                min = dist[i]
                u = i
        # 결정
        selected[u] = True
        cnt += 1
        # 간선완화
        for w, cost in adj[u]:  # 도착정점 w, 가중치 cost
            if dist[w] > dist[u] + cost:
                dist[w] = dist[u] + cost

    print('#{} {}'.format(tc+1, dist[-1]))
```



### 문자열 탐색

### 동적 계획법의 소개

### 동적 계획법의 적용

### 동적 계획법의 활용

### NP-Complete

### 근사 알고리즘