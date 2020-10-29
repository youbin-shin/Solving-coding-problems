def solution(clothes):
    answer = 1
    clothes_list = []
    for i in range(len(clothes)): # 옷 종류마다 몇 개가 있는지 조사
        if clothes[i][1] in clothes_list:
            idx = clothes_list.index(clothes[i][1]) + 1
            clothes_list[idx] += 1
        else:
            clothes_list.extend([clothes[i][1], 1])

    if len(clothes_list) == 2: # 옷 종류가 1개 일 경우 그 옷의 종류의 개수가 정답
        answer = clothes_list[1]
    else: # 옷의 종류가 2개 이상일 경우 옷 개수에 + 1을 하여 경우의 수를 다 구해주기
        for j in range(1, len(clothes_list)+1, 2):
            answer *= (clothes_list[j]+1)
        answer -= 1 # 옷을 아예 안입는 경우 제외
    return answer

    
clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))