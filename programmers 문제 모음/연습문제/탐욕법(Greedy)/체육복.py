def solution(n, lost, reserve):
    answer = n - len(lost) # 현재 체육복을 안잃어버린 학생 수 answer에 저장

     # lost, reserve에 모두 있는 학생은 제외하기
    temp = []
    for i in lost:
        if i in reserve:
            reserve.pop(reserve.index(i))
            temp.append(i)
            answer += 1
    while temp:
        lost.pop(lost.index(temp.pop()))

    # 정렬 후 체육복 빌려줄 수 있는 경우 구하기
    lost.sort()
    reserve.sort()
    reserve_check = [True] * len(reserve) # 이미 빌려준 체육복인지 확인하는 리스트
    for l in range(len(lost)):
        for r in range(len(reserve)):
            if reserve_check[r] and (lost[l]-1 == reserve[r] or lost[l] +1 == reserve[r]):
                reserve_check[r] = False
                answer += 1
                break
    return answer


# n = 5
# lost = [4, 2, 3]
# reserve = [3]
# print(solution(n, lost, reserve))