from itertools import combinations

# 입력 받기
N, M = map(int, input().split())
city_info = [list(map(int, input().split())) for _ in range(N)]

# 집인 경우, 치킨 집인 경우 리스트로 저장하기
house_list = []
chicken_list = []
for i in range(N):
    for j in range(N):
        if city_info[i][j] == 1:
            house_list.append([i, j])
        elif city_info[i][j] == 2:
            chicken_list.append([i, j])

# 계산하기
chicken_final_list = list(combinations(chicken_list, M)) # 치킨 집을 M개만 남기기에 조합으로 가능한 리스트 저장하기
final_distance = 99999999 
for ck in range(len(chicken_final_list)): # 치킨 집 조합 후보(리스트)를 완전 탐색!
    ck_lst = chicken_final_list[ck]
    distance = 0
    for h in range(len(house_list)): # 도시의 집 리스트를 통해 치킨 거리를 계산하기
        temp = 9999999
        h_x = house_list[h][0]
        h_y = house_list[h][1]
        for c in range(len(ck_lst)): 
            c_x = ck_lst[c][0]
            c_y = ck_lst[c][1]
            cal_distance = abs(h_x - c_x) + abs(h_y - c_y)
            if temp > cal_distance: # 치킨 집 중 가장 거리가 작은 치킨 거리를 저장하기
                temp = cal_distance
        distance += temp # 모든 도시의 치킨 거리를 더하기
    if final_distance > distance: # 모든 경우 중에서 가장 작은 치킨 거리를 계산하기
        final_distance = distance
print(final_distance)