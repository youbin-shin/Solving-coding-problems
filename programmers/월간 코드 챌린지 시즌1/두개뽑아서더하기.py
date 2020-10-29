def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            temp = numbers[i] + numbers[j]
            if temp not in answer:
                answer.append(temp)
    answer.sort()
    return answer


# numbers = [2, 1, 3, 4, 1]
# print(solution(numbers))