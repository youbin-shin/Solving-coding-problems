def solution(line):
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

    x_length, y_length = 1, 1
    if min_x != max_x:
        x_length = max_x - min_x + 1
    if min_y != max_y:
        y_length = max_y - min_y + 1

    answer = ["." * x_length for _ in range(y_length)]
    # 2. 좌표에 * 찍기
    for x, y in point_list:
        answer[max_y - y] = (
            answer[max_y - y][: x - min_x] + "*" + answer[max_y - y][x - min_x + 1 :]
        )
    for a in range(len(answer)):
        answer[a] = "".join(answer[a])
    return answer
