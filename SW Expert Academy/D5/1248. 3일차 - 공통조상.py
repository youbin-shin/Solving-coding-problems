 # x에 대한 부모 노드를 찾고 그 과정을 lst에 저장하는 함수
def find_set(x, lst):
    if p[x] == x:
        lst.append(p[x])
        return
    else:
        lst.append(p[x])
        return find_set(p[x], lst)

    
# 자식, 부모 관계를 연결해주는 함수
def union(x, y): 
    p[y] = x


for tc in range(int(input())):
    # 입력
    V, E, v1, v2 = map(int, input().split())
    Elst = list(map(int, input().split()))
    p = [x for x in range(V+1)]
    for i in range(0, len(Elst), 2):
        union(Elst[i], Elst[i+1])
    v1_parent = []
    v2_parent = []
    find_set(v1, v1_parent)
    find_set(v2, v2_parent)
	# result : 가장 가까운 공통 조상 정점 저장
    result = 0
    for j in range(len(v1_parent)):
        if result > 0: break
        for k in range(len(v2_parent)):
            if v1_parent[j] == v2_parent[k]:
                result = v2_parent[k]
                break
    if result == 1: 
        cnt = 0
    else:
        cnt = 3 # 가장 가까운 공통 조상 점정이 1이 아니면 v1, v2, result 노드를 카운트 해줘야한다.
    for k in range(1, V+1):
        lst_parent = []
        find_set(p[k], lst_parent)
        if result in lst_parent:
            cnt += 1
    print('#{} {} {}'.format(tc+1, result, cnt))