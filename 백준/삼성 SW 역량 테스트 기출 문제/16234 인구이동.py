def search(y, x, num): # 연합가능한 나라 찾는 함수
    global visited, union_people, union_list
    q = [[y, x]]
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    while q:
        oy, ox = q.pop(0)
        for d in range(4):
            ny = oy + dirs[d][0]
            nx = ox + dirs[d][1]
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == -1:
                diff = abs(country[oy][ox] - country[ny][nx])
                if L <= diff <= R:
                    union_list[num].append([ny, nx])
                    union_people[num] += country[ny][nx]
                    visited[ny][nx] = num
                    q.append([ny, nx])


# 입력받기
N, L, R = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(N)]

move_cnt = 0
while True:
    visited = [[-1] * N for _ in range(N)]
    num = -1
    union_list = [] # 연합으로 묶일 나라들 저장하는 리스트
    union_people = [] # 연합할 경우 연합한 나라의 인구수를 저장하는 리스트
    # 연합가능하나라 찾기
    for y in range(N):
        for x in range(N):
            if visited[y][x] == -1:
                num += 1
                union_list.append([[y, x]])
                union_people.append(country[y][x])
                visited[y][x] = num
                search(y, x, num)

    # 연합한 나라 인구 새로 저장해주기
    frag = False
    for i in range(num + 1):
        if len(union_list[i]) != 1:
            frag = True
            people = int(union_people[i] // len(union_list[i]))
            for j in range(len(union_list[i])):
                uy, ux = union_list[i][j][0], union_list[i][j][1]
                country[uy][ux] = people
    if frag == False: # 만약 인구이동이 없을 경우 종료 조건
        break
    move_cnt += 1
print(move_cnt)