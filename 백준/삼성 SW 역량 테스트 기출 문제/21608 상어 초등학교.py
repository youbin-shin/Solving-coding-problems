N = int(input())
rooms = [[0 for _ in range(N)] for _ in range(N)]

student = []
like_students = []
for _ in range(N * N):
    a = list(map(int, input().split()))
    student.append(a[0])
    like_students.append(a[1:])

dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for n in range(N * N):
    s = student[n]
    maybe = []
    for y in range(N):
        for x in range(N):
            likes = 0
            empty = 0
            if rooms[y][x] == 0:
                for d in range(4):
                    ny, nx = y + dirs[d][0], x + dirs[d][1]
                    if 0 <= ny < N and 0 <= nx < N:
                        if rooms[ny][nx] == 0:
                            empty += 1
                        elif rooms[ny][nx] in like_students[n]:
                            likes += 1
                maybe.append([likes, empty, y, x])
    choose = sorted(maybe, key = lambda x : (-x[0], -x[1], x[2], x[3]))
    pick_y, pick_x = choose[0][2], choose[0][3]
    rooms[pick_y][pick_x] = s

final_heart = 0
for y in range(N):
    for x in range(N):
        s = rooms[y][x]
        idx = student.index(s)
        cnt = 0
        for d in range(4):
            ny, nx = y + dirs[d][0], x + dirs[d][1]
            if 0 <= ny < N and 0 <= nx < N:
                if rooms[ny][nx] in like_students[idx]:
                    cnt += 1
        if cnt < 2:
            final_heart += cnt
        elif cnt == 2:
            final_heart += 10
        elif cnt == 3:
            final_heart += 100
        else:
            final_heart += 1000

print(final_heart)