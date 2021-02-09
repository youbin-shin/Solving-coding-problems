def check(): # 사다리 조작이 원하는 대로 됐는지 확인하는 함수
    for c in range(N): # 사다리 타기
        person = c 
        for r in range(H):
            if 0 <= person - 1 < N - 1 and ladder[r][person - 1] == 1: # 가로선이 있는 경우 이동시키기
                person -= 1
            elif 0 <= person < N - 1 and ladder[r][person] == 1: # 가로선이 있는 경우 이동시키기
                person += 1
        if person != c: # 사다리 조작이 원하는 대로 안되는 경우
            return 0 
    return 1 # 원하는 사다리 조작이 된 경우


def setLadder(plus, max_plus, start):
    global answer
    if plus == max_plus: # 추가하려는 가로선의 수가 채워진다면
        if check(): # 사다리 조작이 원하는 대로 됐는지 확인하는 함수
            # 원하는 사다리 조작이 완료됐다면 추가한 가로선을 answer에 저장하여 종료하기
            answer = plus
        return
    # 가로선 추가하기
    for y in range(start, H):
        for x in range(N - 1):
            if ladder[y][x] != 1: # 가로선 추가가능한 경우
                if x - 1 > 0 and ladder[y][x - 1] == 1: # 연속적인 가로선으로 추가 불가한 경우
                    continue
                if x + 1 < N - 1 and ladder[y][x + 1] == 1: # 연속적인 가로선으로 추가 불가한 경우
                    continue
                ladder[y][x] = 1
                setLadder(plus + 1, max_plus, y) # 가로선 추가하여 백트래킹 이용!
                ladder[y][x] = 0


N, M, H = map(int, input().split())
ladder = [[0] * (N - 1) for _ in range(H)] # 사다리의 가로선의 유무를 저장하는 이중 리스트
for _ in range(M): # 주어진 가로선 정보 저장하기
    h, n = map(int, input().split())
    ladder[h - 1][n - 1] = 1

answer = -1
for p in range(4): # 가로선 최대로 3개까지 추가할 수 있기에!
    if answer != -1: break # 추가해야 하는 가로선 최솟값을 구하는 것이기에 구했으면 종료하기
    setLadder(0, p, 0) # 사다리 가로선 세팅하는 함수

print(answer)