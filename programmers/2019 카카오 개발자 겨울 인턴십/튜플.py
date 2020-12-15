def solution(s):
    s_list = []
    for i in map(str, s.split("}")): # s_list에 집합 형태를 리스트로 저장
        if i == "":
            break
        s_list.append(list(map(int, i[2:].split(","))))
    s_list.sort(key=len) # 원소의 길이가 짧은 순서로 정렬

    answer = []
    for lst in s_list:
        for j in lst:
            if j not in answer:
                answer.append(j)
    return answer


# s = "{{2},{2,1,3},{2,1,3,4},{2,1}}"
# print(solution(s))