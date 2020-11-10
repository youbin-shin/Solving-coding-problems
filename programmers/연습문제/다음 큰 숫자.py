def solution(n):
    n_one = list(map(int, bin(n)[2:])).count(1)
    while True:
        n += 1
        if n_one == list(map(int, bin(n)[2:])).count(1):
            answer = n
            break
    return answer


n = 78
print(solution(n))