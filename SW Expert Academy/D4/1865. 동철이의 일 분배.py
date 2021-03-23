## 재귀를 이용한 순열
## 기본 코드 형태
# def f(n, k):
#     if n == k:
#         ...
#     else:
#         for i in range(k):
#             if used[i] == 0:
#                 used[i] = 1
#                 p[n] = a[i]
#                 f(n+1, k)
#                 used[i] = 0 # ★ 간과하고 있었던 부분

## => 재귀로 완전탐색을 할 경우 펙토리얼이기에 16! = 20,922,789,888,000 무리..

def select(n, N, result, visit):
    global fresult
    if n == N:
        if fresult < result:
            fresult = result

    if fresult >= result: # = 가 없으면 fail!!★
        return
    else:
        for i in range(N):
            if visit[i] == 0:
                visit[i] = 1
                select(n+1, N, result*P[i][n]/100, visit)
                visit[i] = 0


for t in range(1, int(input()) + 1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    fresult = 0
    visit = [0] * N
    select(0, N, 1, visit)
    print('#{} {:.6f}'.format(t, fresult*100))