for tc in range(10):
    vertex, line = map(int, input().split())
    G = [[0]*(vertex+1) for _ in range(vertex+1)]
    lines = list(map(int, input().split()))
    visited = [0] * (vertex + 1)
    stack = []

    for i in range(0,len(lines),2):
        G[lines[i]][lines[i+1]] = 1
        visited[lines[i+1]] += 1

    for i in range(1, vertex+1):
        if visited[i] == 0:
            stack.append(i)
            visited[i] = 1

    result = []
    while len(stack):

        v = stack.pop(-1)

        visited[v] -= 1
        if visited[v] == 0:
            result.append(v)    
            for w in range(1, len(G[v])):
                if G[v][w] == 1 and visited[w] != 0:
                    stack.append(w)

    print('#{}'.format(tc+1), end=' ')
    for i in range(len(result)):
        print(result[i], end =' ')
    print()