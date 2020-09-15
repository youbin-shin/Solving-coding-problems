def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i != len(arr)-1 and arr[i] == arr[i+1]:
            continue
        else: answer.append(arr[i])

    return answer