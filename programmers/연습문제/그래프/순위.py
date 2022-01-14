# 플로이드 와샬 알고리즘 

def solution(n, results):
    # 1. 승리, 패배에 대한 결과 저장
    rank = [[None] * n for _ in range(n)]
    for win, lose in results:
        rank[win - 1][lose - 1] = True
        rank[lose - 1][win - 1] = False
    
    # 2. 유추가능한 순위있는지 체크
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if rank[i][j] == None:
                    continue
                # 같은 결과일 경우 확실한 결과 예측 가능(i > j: i승, j패)
                # case 1. i > j and j > k => i > k
                # case 2. i < j and j < k => i < k 
                if rank[i][j] == rank[j][k]:
                    rank[i][k] = rank[i][j]
                    rank[k][i] = not rank[i][j]

    # 3. 행에 None이 하나(자기자신과의 순위)일 경우 정확한 순위
    answer = 0
    for i in range(n):
        if rank[i].count(None) == 1:
            answer += 1
    return answer