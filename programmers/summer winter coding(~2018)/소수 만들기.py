from itertools import combinations

def solution(nums):
    answer = 0
    # 주어진 숫자 중 3개를 더하는 모든 경우를 sum_list에 저장하기
    sum_list = list(sum(lst) for lst in combinations(nums, 3))

    # 소수인지 확인하는 코드
    for s1 in sum_list:
        check = True
        for s2 in range(2, s1):
            if s1 % s2 == 0: # 소수가 아닌 경우
                check = False
                break
        if check: # 소수인 경우 정답 1 증가
            answer += 1
    return answer