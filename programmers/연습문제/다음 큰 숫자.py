def solution(n):
    n_one = list(map(int, bin(n)[2:])).count(1) # 2진수로 변환 후 1의 갯수 저장
    while True:
        n += 1 # 조건 1 : n보다 큰 자연수
        if n_one == list(map(int, bin(n)[2:])).count(1): # 조건 2 : 2진수 변환 후 1의 개수가 같은 경우
            answer = n
            break
    return answer


n = 78
print(solution(n))