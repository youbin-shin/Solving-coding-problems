def solution(n):
    batteryCnt = 0 # 건전지 사용 횟수 저장하는 변수
    while n:
        # 2배 이동이 가능한 경우 순간 이동이 효율적
        if n % 2 == 0: 
            n = n // 2
        
        # 점프를 해야하는 경우 건전지 최소로 사용을 위해 1 점프
        else:
            n -= 1
            batteryCnt += 1
    return batteryCnt


# n = 5000
# print(solution(n))