import heapq

for tc in range(int(input())):
    # 입력받기
    V = int(input())
    adj = {i: [] for i in range(V)}  # 인접리스트
    xlst = list(map(int, input().split()))
    ylst = list(map(int, input().split()))
    tax = float(input())
    for i in range(V):
        for j in range(i+1, V):
            s, e = i, j # 시작정점, 끝정점
            c = ((xlst[s]-xlst[e])*(xlst[s]-xlst[e]) + (ylst[s]-ylst[e])*(ylst[s]-ylst[e])) * tax #가중치
            adj[s].append([e, c])
            adj[e].append([s, c])
    # 계산하기
    # key, mst, 우선순위 큐 준비
    INF = float('inf')
    key = [INF] * V
    mst = [False] * V
    pq = []
    # 시작점 선택 : 0번 선택
    key[0] = 0
    heapq.heappush(pq, (0, 0))
    result = 0
    while pq:
        # 최소값 찾기
        k, node = heapq.heappop(pq)  # 가장 작은값 꺼낸다. (key, u)
        if mst[node]: continue  # old 한 정보면 스킵
        # mst로 선택
        mst[node] = True
        result += k
        # key 값을 갱신 => key 배열/큐
        for dest, wt in adj[node]:  # dest 가고자하는 곳, wt 가중치
            if not mst[dest] and key[dest] > wt:
                key[dest] = wt
                # 큐 갱신 => 새로운 (key, 정점) 삽입 (필요없는 원소는 스킵)
                heapq.heappush(pq, (key[dest], dest))
    print('#{} {}'.format(tc+1,int(result+0.5))) # 반올림해주기!!