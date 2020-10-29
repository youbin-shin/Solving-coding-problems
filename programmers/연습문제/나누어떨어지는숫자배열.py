def solution(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor == 0: # 나누어지면 answer에 저장
            answer.append(a)
    answer.sort() # 오름차순 정렬
    if len(answer) == 0: answer = [-1]
    return answer