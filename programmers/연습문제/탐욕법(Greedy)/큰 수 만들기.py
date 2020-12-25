def solution(number, k):
    answer = [number[0]]
    for num in number[1:]:
        # 가장 큰 수가 되기 위해 제거해야 할 조건
        while len(answer) > 0 and answer[-1] < num and k > 0: 
            k -= 1
            answer.pop() 
        answer.append(num) 
    if k != 0: # 제거해야할 수가 남아있으면 뒤에서 자르기
        answer = answer[:-k]
    answer = "".join(answer)
    return answer


# number = "4177252841"
# k = 4
# print(solution(number, k))