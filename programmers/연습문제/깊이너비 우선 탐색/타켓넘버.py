def solution(numbers, target):
    result = [0] # 계산될 수 있는 모든 경우를 저장하는 리스트
    for i in range(len(numbers)):
        n = len(result)
        for j in range(n):
            temp = result[j]
            result[j] += numbers[i] # 더하는 경우
            result.append(temp - numbers[i]) # 빼는 경우
    answer = result.count(target)
    return answer


# numbers = [1, 1, 1, 1, 1]
# target = 3
# print(solution(numbers, target))