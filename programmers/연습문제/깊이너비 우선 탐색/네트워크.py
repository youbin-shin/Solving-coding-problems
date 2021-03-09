from collections import deque

def solution(n, computers):
    visited = [False] * n # 네트워크에 연결됐는지 확인하는 리스트
    q = deque([0])
    k = 1 # 네트워크에 포함된 컴퓨터 수 저장 변수
    answer = 1 # 네트워크 개수 저장하는 변수
    while k <= n: # 컴퓨터가 네트워크에 모두 포함될 때까지
        if len(q) == 0: # 네트워크 추가 필요!!
            answer += 1
            for v in range(n):
                # 아직 네트워크 연결안된 컴퓨터 하나 찾아서 q에 삽입
                if visited[v] == False:
                    q.append(v)
                    break
        # BFS를 이용하여 연결된 네트워크 탐색하기
        c = q.popleft()
        for i in range(n):
            if computers[c][i] == 1 and visited[i] == False:
                q.append(i)
                visited[i] = True
                k += 1
    return answer


# n = 3
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
# print(solution(n, computers))