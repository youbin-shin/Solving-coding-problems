def solution(dirs):
    location = set()
    x, y = 0, 0 # 현재 위치
    nx, ny = 0, 0 # 이동할 위치
    for d in dirs:
        if d == "U" and y + 1 <= 5:
            ny = y + 1
        elif d == "L" and x - 1 >= -5:
            nx = x - 1
        elif d == "R" and x + 1 <= 5:
            nx = x + 1
        elif d == "D" and y - 1 >= -5:
            ny = y - 1
        # location에 간 길(출발지, 도착지) 저장하기
        if (x, y) != (nx, ny):
            location.add((x, y, nx, ny))
            location.add((nx, ny, x, y))
            x, y = nx, ny
    return len(location) // 2


# dirs = "LULLLLLLU"
# dirs = "ULURRDLLU"
# print(solution(dirs))