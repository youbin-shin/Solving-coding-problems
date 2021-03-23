# sol 1
# DFS에서의 Q의 개념과 Dijkstra 를 이용하여 해결한 코드

for tc in range(int(input())):
    N = int(input())
    road = [list(map(int, input())) for _ in range(N)] # 보급로관련 데이터받기
    INF = float('inf')
    dist = [[INF] * N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append([0, 0])
    dist[0][0] = road[0][0]
    while q:
        x, y = q.pop(0)
        visited[x][y] = 1
        dir = [[1, 0], [0, -1], [-1, 0], [0, 1]]
        for d in range(4):
            nx = x + dir[d][0]
            ny = y + dir[d][1]
            if 0<=nx<N and 0<=ny<N: 
                if dist[nx][ny] > dist[x][y] + road[nx][ny]: # 비교하며 업데이트
                    dist[nx][ny] = dist[x][y] + road[nx][ny]
                    q.append([nx, ny])
    print('#{} {}'.format(tc+1, dist[N-1][N-1]))


# # sol 2
# # 누적합 이용
# for t in range(int(input())):
#     N, M = map(int, input().split())
#     arr = [input() for _ in range(N)]

#     w = [0] * N
#     b = [0] * N
#     r = [0] * N
#     for i in range(N):
#         w[i] = arr[i].count('W')
#         b[i] = arr[i].count('B')
#         r[i] = M - w[i] - b[i]

#     for i in range(1, N):
#         w[i] += w[i - 1]
#         b[i] += b[i - 1]
#         r[i] += r[i - 1]

#     ans = N * M
#     for i in range(0, N-3+1):
#         for j in range(i+1, N-2+1):
#             # 전체 칸 수 에서 바꿀 필요 없는 칸수 빼서 구하기
#             cnt = M * (i+1) - w[i]
#             cnt += M * (N - 1 - (j+1) + 1) - (r[N-1] - r[j])

#             ans = min(ans, cnt)
#     print('#{} {}'.format(t+1,ans))