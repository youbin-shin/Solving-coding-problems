def solution(citations):
    answer = 0
    for i in range(max(citations), -1, -1):
        cnt = 0
        for j in range(len(citations)):
            if i <= citations[j]: cnt += 1
        if i <= cnt and cnt >= len(citations) - cnt:
            answer = i
            break
    return answer


# citations = [3, 0, 6, 1, 5]
# citations = [0, 0, 1, 1]
# print(solution(citations))