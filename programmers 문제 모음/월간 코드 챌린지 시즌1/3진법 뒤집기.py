def solution(n):
    n_three = "" 
    # n을 3진법 한 결과를 반전해서 저장하기
    while n:
        n_three += str(n % 3)
        n = int(n // 3)
    n_three = str(int(n_three))

    n_ten = 0
    idx = 1
    for i in range(len(n_three)-1, -1, -1): # 10진법으로 표현
        n_ten += int(n_three[i]) * idx
        idx *= 3
    return n_ten


# n = 45
# print(solution(n))