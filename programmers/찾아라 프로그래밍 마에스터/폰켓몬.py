def solution(nums):
    set_nums = set(nums) # 포켓몬 종류 중복 제거
    N = len(nums) // 2 # 선택가능한 포켓몬 수
    if len(set_nums) >= N: # 선택가능한 종류보다 선택가능한 포켓몬 수가 적을 경우
        answer = N
    else: # 선택가능한 종류보다 선택가능한 포켓몬 수가 많은 경우 
        answer = len(set_nums)
    return answer


# nums = [3, 1, 2, 3]
# print(solution(nums))