def springSummer(): # 봄과 여름에 일어나는 동작을 수행하는 함수
    fall_tree = [] # 가을에 번식할 나무 위치 저장하는 리스트
    for r in range(N):
        for c in range(N):
            if tree[r][c] != []: # 나무가 존재하는 경우
                tree[r][c].sort() # 나무 나이 어린 순으로 정렬
                die_check = False # 나무가 죽는지 체크하는 변수 (summer 의 동작이 일어날지의 유무 결정)
                die_idx = 0 # 나무가 죽는 경우 맨 처음에 죽는 나무 인덱스

                tree_num = len(tree[r][c])
                # 1. 봄에 일어나는 동작
                for t in range(tree_num):
                    if land[r][c] >= tree[r][c][t]:
                        land[r][c] -= tree[r][c][t] # 나무가 자신의 나이만큼 양분 먹기
                        tree[r][c][t] += 1 # 나무 나이 1 증가
                        if tree[r][c][t] % 5 == 0: # 5의 배수
                            fall_tree.append([r, c])
                    else: # 양분을 먹지 못하고 죽음
                        if die_check == False: # 맨 처음에 죽는 나무의 인덱스를 저장하기 위한 조건
                            die_idx = t
                        die_check = True
                # 여름에 일어나는 동작
                if die_check: # 죽은 나무가 있는 경우만 동작하기에 분기하기
                    for d in range(die_idx, tree_num):
                        land[r][c] += int(tree[r][c][d] / 2) # 죽은 나무 양분으로 추가하기
                    tree[r][c] = tree[r][c][:die_idx] # 죽은 나무 제거하기

    fall(fall_tree) # 가을에 일어나는 동작 수행하는 함수


def fall(fall_tree): # 가을에 일어나는 동작 수행하는 함수
    dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for f in range(len(fall_tree)): # 나무의 나이가 5의 배수가 넘는 나무들 번식하기
        y, x = fall_tree[f][0], fall_tree[f][1]
        for d in range(8):
            ny, nx = y + dirs[d][0], x + dirs[d][1]
            if 0 <= ny < N and  0 <= nx < N:
                tree[ny][nx].append(1)
    winter() # 겨울에 일어나는 동작 수행하는 함수

def winter(): # 겨울에 일어나는 동작 수행하는 함수
    for i in range(N):
        for j in range(N):
            land[i][j] += land_food[i][j] # 양분 더하기


# 입력받기
N, M, K = map(int, input().split())
land = [list(5 for _ in range(N)) for _ in range(N)] # 땅의 양분의 양을 저장하는 리스트
tree = [[[] for _ in range(N)]  for _ in range(N)] # 나무 나이를 저장할 리스트
land_food = [list(map(int, input().split())) for _ in range(N)] # 겨울에 더해야하는 양분을 저장한 리스트
# 나무 위치에 나무 나이 저장하기
for _ in range(M):
    y, x, z = map(int, input().split())
    tree[y - 1][x - 1].append(z)
    
for _ in range(K):
    springSummer() # 봄과 여름에 일어나는 동작을 수행하는 함수

# 최종 결과 출력하기
tree_sum = 0
for r in range(N):
    for c in range(N):
        if tree[r][c] != []:
            tree_sum += len(tree[r][c]) # 나무의 수 더하기
print(tree_sum)