def solution(maps):
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    width = len(maps[0])
    height = len(maps)
    visited = [[0] * width for _ in range(height)]
    q = [[0, 0]]
    visited[0][0] = 1
    visited[height - 1][width - 1] = -1
    while q:
        y, x = q.pop(0)
        for d in range(4):
            ny, nx = y + dirs[d][0], x + dirs[d][1]
            if 0 <= ny < height and 0 <= nx < width and maps[ny][nx]:
                if visited[ny][nx] <= 0:
                    visited[ny][nx] = visited[y][x] + 1
                    for d2 in range(4):
                        ny2, nx2 = ny + dirs[d2][0], nx + dirs[d2][1]
                        if 0 <= ny2 < height and 0 <= nx2 < width and visited[ny2][nx2] > 0 and [ny2, nx2] != [y, x]:
                            visited[ny][nx] = min(visited[ny][nx], visited[ny2][nx2] + 1)
                    q.append([ny, nx])

    return visited[height - 1][width - 1]