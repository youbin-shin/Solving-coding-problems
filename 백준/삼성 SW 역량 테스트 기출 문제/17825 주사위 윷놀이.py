from copy import deepcopy

def play(n, score, horse):
    global max_score
    if n == 10: # 모든 게임의 천이 끝난 종료 조건
        if score > max_score:
            max_score = score
        return

    # 4개의 말에 대해 각각 이동을 시킴으로써 완전 탐색을 진행하기
    for h in range(4):
        if horse[h][0] != -1: # 도착칸에 있는 말이 아닌 경우
            temp = deepcopy(horse)
            temp[h][0] += dice[n] # 주사위만큼 이동하기

            # 파란칸 위인지 확인하기
            if temp[h][1] == 0:
                if temp[h][0] == 5: # 점수가 10인 지점
                    temp[h][1] = 1 # road[1]의 길을 가기 때문에
                    temp[h][0] = 0
                elif temp[h][0] == 10: # 점수가 20인 지점
                    temp[h][1] = 2 # road[2]의 길을 가기 때문에
                    temp[h][0] = 0

                elif temp[h][0] == 15: # 점수가 30인 지점
                    temp[h][1] = 3 # road[3]의 길을 가기 때문에
                    temp[h][0] = 0

            # 도착지점에 온 말인지 체크하기
            if temp[h][0] >= len(road[temp[h][1]]):
                temp[h][0] = -1 # 말이 도착했다고 체크하기
                play(n + 1, score, temp)
            else:
                # 이동하려는 곳에 말이 있으면 이동하지 않는다! ★
                frag = False # 이동하려는 칸에 말이 있는지 체크할 변수
                visit = road[temp[h][1]][temp[h][0]] # 움직이려는 말이 있는 점수판의 점수
                for v in range(len(temp)):
                    if temp[v][0] == -1: continue # temp[v][1]로 잘못 써서 26%에서 틀렸었다..!! 조심하기
                    if v != h and visit == road[temp[v][1]][temp[v][0]]:
                        if visit == 30: # 30의 경우 road에 여러개가 있기에 같은 위치인지 분기를 잘 해야한다.
                            if temp[h] == [0, 3] and temp[v] == [0, 3]:
                                frag = True
                                break
                            elif temp[h] != [0, 3] and temp[v] != [0, 3]:
                                frag = True
                                break
                        # len(road) = 4개의 길 중 해당 숫자는 2개 겹치기에 같은 위치인지 확인하기
                        elif visit in [16, 22, 24, 26, 28]:
                            if temp[h] == temp[v]:
                                frag = True
                                break
                        else: # 그 외의 숫자는 게임판에 각 1개 이기에 같기만 하면 같은 위치라 볼 수 있다.
                            frag = True
                            break
                if frag: # 이동하려는 칸에 다른 말이 있기에 스킵하기
                    continue
                play(n + 1, score + road[temp[h][1]][temp[h][0]], temp)


# road : 게임판의 점수를 저장한 리스트
# road[0] : 가장 바깥 테두리 부분의 길 (파란색 칸에 도착한 적 X)
# road[1] : 점수 10의 파란색 칸에 도달했을 때 도착지까지 남은 길
# road[2] : 점수 20의 파란색 칸에 도달했을 때 도착지까지 남은 길
# road[0] : 점수 30의 파란색 칸에 도달했을 때 도착지까지 남은 길
road = [
    [i * 2 for i in range(21)],
    [10, 13, 16, 19, 25, 30, 35, 40],
    [20, 22, 24, 25, 30, 35, 40],
    [30, 28, 27, 26, 25, 30, 35, 40]
]

max_score = 0 # 최대 점수로 출력값
horse = [[0, 0] for _ in range(4)] # 4개의 말에 대한 정보를 저장할 리스트
# horse 리스트안에 요소의 의미 : [해당 road에 대한 인덱스(위치), 어떤 road인지]

dice = list(map(int, input().split()))
play(0, 0, horse) # 모든 경우의 윷놀이를 진행할 함수
print(max_score)