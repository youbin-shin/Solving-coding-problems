def solution(places):
    answer = []
    N = 5

    def check_seat(place, y, x):
        # place[y][x]의 응시자가 올바른 거리 두기를 했는지 확인하는 함수
        seats_dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for d in range(4):
            ny, nx = y + seats_dirs[d][0], x + seats_dirs[d][1]
            if 0 <= ny < N and 0 <= nx < N:
                if place[ny][nx] == "P":
                    return False
                elif place[ny][nx] == "O":
                    for d2 in range(4):
                        ny2, nx2 = ny + seats_dirs[d2][0], nx + seats_dirs[d2][1]
                        if [ny2, nx2] != [y, x] and 0 <= ny2 < N and 0 <= nx2 < N and place[ny2][nx2] == "P":
                            return False
        return True

    for place in places:
        result = 1
        for y in range(N):
            for x in range(N):
                if place[y][x] == "P":
                    is_able = check_seat(place, y, x)
                    if not is_able:
                        result = 0
                        break
            if not result:
                break
        answer.append(result)
    return answer