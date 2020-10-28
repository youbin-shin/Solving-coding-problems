def solution(x):
    answer = False
    num_sum = 0
    num = x

    while x != 0:
        q, r = divmod(x, 10)
        x = q
        num_sum += r
    if num % num_sum == 0: answer = True
    return answer


# x = 10
# print(solution(x))