def solution(triangle):
    height = len(triangle)
    triangle.append([0]*(height + 1))
    # 거쳐간 숫자의 합이 가장 큰 경우를 누적하여 계산하기
    for h in range(height):
        for i in range(h + 2):
            if i == 0: # 맨 처음 값
                triangle[h + 1][i] += triangle[h][i]
            elif i == h + 1: # 맨 마지막 값
                triangle[h + 1][i] += triangle[h][i - 1]
            else: # 중간 값
                triangle[h + 1][i] += max(triangle[h][i], triangle[h][i - 1])
    return max(triangle[height])


# triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
# print(solution(triangle))