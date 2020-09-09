from itertools import combinations

def solution(relation):
    answer = 0
    N = len(relation[0])
    people = len(relation)
    lst = [i for i in range(N)]

    candidate_list = []
    for i in range(1, N+1): # 후보키가 가능한 조합을 모두 candidate_list에 저장
        candidate_list += [list(x) for x in combinations(lst, i)]
    visited = [True] * len(candidate_list) # 최소성을 만족하는지를 구별하기 위해 visited 이용

    for j in range(len(candidate_list)):
        check = [] 
        if visited[j]: # 최소성을 만족(True)하는 조건
            for k in range(len(relation)):
                temp = []
                for j2 in range(len(candidate_list[j])):
                    temp.append(relation[k][candidate_list[j][j2]])
                # 후보키에 해당하는 값을 저장
                if temp not in check:
                    check.append(temp)
                else:
                    break
            if len(check) == people: # 유일성 식별 완료 
                # 최소성을 만족하기 위해 candidate_list[j]를 포함하는 후보키들은 False로 표시
                num1 = len(candidate_list[j])
                for j3 in range(j+1, len(candidate_list)):
                    cnt = 0
                    for j4 in candidate_list[j]:
                        if j4 in candidate_list[j3]:
                            cnt += 1
                    if cnt == len(candidate_list[j]):
                        visited[j3] = False
                answer += 1
                # print(check)

    return answer


# testcase 1
# relation = [["b","2","a","a","b"], ["b","2","7","1","b"], ["1","0","a","a","8"], ["7","5","a","a","9"], ["3","0","a","f","9"]] # answer 5
# testcase 2
# relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
# print(solution(relation))