# 이동 방향은 오른쪽, 아래 두가지 경우이기 때문에 아래와 같이 계산된다.
# road[y][x] = road[y  -1][x] + road[y][x - 1]

def solution(m, n, puddles):
    road = [[0] * m for _ in range(n)]
    real_puddles = []
    for puddle in puddles:
        x, y = puddle
        real_puddles.append([y - 1, x - 1])
    road[0][0] = 1
    for y in range(n):
        for x in range(m):
            if [y, x] == [0, 0]:
                continue
            if [y, x] in real_puddles:
                continue
            elif y == 0:
                road[y][x] = road[y][x - 1]
            elif x == 0:
                road[y][x] = road[y - 1][x]
            else:
                road[y][x] = road[y][x - 1] + road[y - 1][x]
    return road[n - 1][m - 1] % 1000000007