def solution(line):
    answer = []
    # 1. 교점 찾기
    line_cnt = len(line)
    point_list = []
    min_x, max_x = float("inf"), -float("inf")
    min_y, max_y = float("inf"), -float("inf")
    for l1 in range(line_cnt):
        for l2 in range(l1 + 1, line_cnt):
            a1, b1, c1 = line[l1]
            a2, b2, c2 = line[l2]
            num = a1 * b2 - a2 * b1
            if num == 0:
                continue
            x = (b1 * c2 - c1 * b2) / num
            y = -(a1 * c2 - a2 * c1) / num
            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y = min(min_y, y)
                max_y = max(max_y, y)
                point_list.append([x, y])
    print(point_list)
    x_length, y_length = 1, 1
    if min_x != max_x:
        x_length = max_x - min_x
    if min_y != max_y:
        y_length = max_y - min_y
    answer = ["." * x_length for _ in range(y_length)]
    zero_x, zero_y = (max_x + min_x) // 2, (max_y + min_y) // 2
    print(zero_x, zero_y)
    for px, py in point_list:
        print(x_length + px, y_length + py, answer[zero_x + px])
        # answer[][] = "*"
    print(answer)
    return answer


line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
print(solution(line))
