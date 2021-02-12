def solution(n, costs):
    costs.sort(key = lambda x: x[2]) # 가중치가 작은 순으로 정렬하기
    p = [i for i in range(n)] 
    tree_edges = 0
    cost = 0

    def find(u): # 연결된 상위 부모노드를 찾아주는 함수
        if u != p[u]:
            p[u] = find(p[u])
        return p[u]

    def union(u, v): # u, v의 섬을 연결해주어 간선이 연결되는 함수
				# 각 섬의 부모 노드를 찾기
        root1 = find(u) 
        root2 = find(v)
        p[root2] = root1 # 부모노드를 갱신하여 간선 연결하기

    while True:
        if tree_edges == n - 1: # mst 조건 : 모든 섬이 통하는 경우
            break
        u, v, wt = costs.pop(0)
        if find(u) != find(v): # 사이클이 아니라면! 연결 가능한 조건
            union(u, v) # 간선 연결하기
            cost += wt # 비용에 가중치 추가하기
            tree_edges += 1 # 간선 추가됨을 확인할 수 있도록 변수에 저장하기
    return cost


# n = 4
# costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
# print(solution(n, costs))