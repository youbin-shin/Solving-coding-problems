from collections import deque

def solution(n, edge):
    # 인접 리스트 이용
    adj = {i: [] for i in range(1, n + 1)}

    for e in edge:
        s, e = e[0], e[1]
        adj[s].append(e)
        adj[e].append(s)

    # visited에 1로 부터 얼마나 떨어져있는지 기록!
    visited = [float('inf')] * (n + 1)
    visited[0] = 0
    visited[1] = 0
    queue = deque([1])

    while queue: # 1로 부터 최단 경로 계산
        top = queue.popleft()
        for w in adj[top]:
            if visited[w] == float('inf'):
                queue.append(w)
                visited[w] = visited[top] + 1
    # 간선의 개수가 가장 많은 노드 찾기
    max_value = max(visited)
    answer = 0
    for i in range(2, n + 1):
        if visited[i] == max_value:
            answer += 1

    return answer


# n = 5
# edge = [[4, 3], [1, 3]]
# print(solution(n, edge))