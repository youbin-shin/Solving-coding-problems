def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else: # 가격이 떨어졌기에 기간 1초 더해주고 끝내기
                answer[i] += 1
                break
    return answer


# prices = [1, 2, 3, 2, 3, 3, 1]
# print(solution(prices))