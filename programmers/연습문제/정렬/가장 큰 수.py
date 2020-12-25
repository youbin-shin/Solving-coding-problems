def solution(numbers):
    numbers = list(map(str, numbers))
    print(numbers)
    # x * 3 : 각각 문자열 3번 반복 => 3자리로 맞춘 뒤 비교
    numbers.sort(key=lambda x: x*3, reverse=True)
    print(numbers)
    return str(int(''.join(numbers)))


numbers = [3, 30, 34, 5, 9]
print(solution(numbers))


## solution 2: 조합을 이용하여 가능하지만 시간 초과 발생
# from itertools import combinations
#
# def solution(number, k):
#     answer = "0"
#     num_list = [i for i in range(len(number))]
#     for num in list(combinations(num_list, len(number) - k)):
#         temp = ""
#         for n in range(len(num)):
#             temp += number[num[n]]
#         if answer < temp:
#             answer = temp
#     return answer