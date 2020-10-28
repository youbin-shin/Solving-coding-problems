def solution(arr):
    arr.pop(arr.index(min(arr))) # arr 가장 작은 값의 인덱스를 찾아 제거
    if len(arr) == 0:# 빈배열일 경우
        answer = [-1]
    else:
        answer = arr
    return answer


# arr = [4, 3, 2, 1]
# print(solution(arr))