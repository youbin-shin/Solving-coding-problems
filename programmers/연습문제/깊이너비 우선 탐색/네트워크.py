def solution(n, computers):
    network = []
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            q = [i]
            temp = [i] # 하나의 네트워크를 이루는 컴퓨터를 기록할 리스트
            while q:
                idx = q.pop(0)
                for j in range(n):
                    if computers[idx][j] == 1 and visited[j] == 0:
                        q.append(j)
                        temp.append(j)
                        visited[j] = 1
            network.append(temp)
    return len(network)


n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))