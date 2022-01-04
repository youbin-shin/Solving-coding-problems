def solution(price, money, count):
    answer = sum([i * price for i in range(1, count + 1)]) - money
    if answer < 0: answer = 0
    return answer