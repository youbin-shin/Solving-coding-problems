def solution(numbers):
    numbers = list(map(str, numbers))
    print(numbers)
    # x * 3 : 각각 문자열 3번 반복 => 3자리로 맞춘 뒤 비교
    numbers.sort(key=lambda x: x*3, reverse=True)
    print(numbers)
    return str(int(''.join(numbers)))


numbers = [3, 30, 34, 5, 9]
print(solution(numbers))