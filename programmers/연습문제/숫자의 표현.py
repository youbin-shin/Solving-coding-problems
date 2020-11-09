def solution(n):
    answer = 1
    for i in range(1, n):
        sum = i
        temp = i
        while True:
            if sum == n: # 원하는 수가 나왔기에 답에 1 더하기
                answer += 1
                break
            if sum > n: # 원하는 수가 표현안되는 경우 종료
                break
            temp += 1
            sum += temp # 연속하여 숫자 더하기
    return answer


n = 20
print(solution(n))