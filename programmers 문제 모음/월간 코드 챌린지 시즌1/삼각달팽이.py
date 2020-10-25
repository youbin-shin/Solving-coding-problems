def solution(n):
    answer = []
    triangle = [[0] * i for i in range(1, n + 1)]
    dirs = [[1, 0], [0, 1], [-1, -1]]
    d = 0
    num = 1
    y, x = 0, 0
    order = [0 for _ in range(n - 1)] # 달팽이가 움질일 방향을 저장할 리스트
    triangle[y][x] = num
    # 삼각방향으로 돌 수 있도록 움직일 방향 저장하기
    for i in range(n - 1, 0, -1):
        d = (d + 1) % 3
        order.extend([d] * i)
    # 순서 저장하기
    for o in order:
        num += 1
        y, x = y + dirs[o][0], x + dirs[o][1]
        triangle[y][x] = num
    for t in range(n):
        answer.extend(triangle[t])
    return answer


# n = 6
# print(solution(n))