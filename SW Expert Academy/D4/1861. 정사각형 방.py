# sol 1
# 재귀함수 이용
# 문제는 통과할 수 있더라도 값의 크기가 커지면 재귀 호출 error 발생
# but, 코드 작성 연습 필요

def move(k, x, y, cnt):
    global fcnt, fk
    dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    for i in range(4):
        nx = x+dir[i][0]
        ny = y+dir[i][1]
        if 0<= nx <N and 0<= ny <N and room[x][y]+1==room[nx][ny]:
            move(k, nx, ny, cnt+1)
    else:
        if cnt > fcnt:
            fcnt = cnt
            fk = k
        if fcnt == cnt and k < fk:
            fk = k

for t in range(1, int(input())):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    fcnt = 0
    fk = N*N
    for x in range(N):
        for y in range(N):
            move(room[x][y], x, y, 0)
    print('#{} {} {}'.format(t, fk, fcnt+1))



## sol 2
# # visited 이용, 시간 짧게 걸림
# dr = [0, 0, 1, -1]
# dc = [1, -1, 0, 0]

# for t in range(int(input())):
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     result = 0
#     result_num = 987654321
#     visited = [0] * (N**2 + 2)
#     for r in range(N):
#         for c in range(N):
#             for i in range(4):
#                 nr = r + dr[i]
#                 nc = c + dc[i]
#                 if 0<=nr<N and 0<=nc<N and board[nr][nc]-board[r][c]==1:
#                     visited[board[nr][nc]] = 1
#     i = 1
#     cnt = 0
#     idx = 1
#     while i <= N ** 2+1:
#         if visited[i] == 1:
#             cnt += 1
#             i += 1
#             continue
#         else:
#             if cnt > result:
#                 result = cnt
#                 result_num = idx
#             if cnt == result:
#                 if result_num > idx:
#                     result_num = idx
#             cnt = 0
#             i += 1
#             idx = i
