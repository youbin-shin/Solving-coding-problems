def solution(strings, n):
    answer = []
    n_list = [] # n에 해당하는 문자와 인덱스 저장한 리스트
    for s in range(len(strings)):
        n_list.append([strings[s][n], s])
    n_list = sorted(n_list, key = lambda x : x[0]) # n에 해당하는 문자 오름차순으로 정렬

    temp = [] # n의 값이 같을 경우 저장하는 리스트
    for n in range(len(n_list)):
        if n != len(n_list)-1 and n_list[n][0] == n_list[n+1][0]: # n의 값이 같으면 temp에 저장
            if strings[n_list[n][1]] in temp: 
                temp.append(strings[n_list[n+1][1]])
            else:
                temp.extend([strings[n_list[n][1]],strings[n_list[n+1][1]]])
        else:
            if temp: # temp 있다면 사전식으로 정렬하여 answer에 저장
                temp.sort()
                answer.extend(temp)
                temp = []
            else:
                answer.append(strings[n_list[n][1]])
    return answer


# strings = 	["abce", "abcd", "cdx", "csx", "adx"]
# n = 2
# print(solution(strings, n))