def solution(answers):
    answer = []
    # 수포자들의 반복되는 답을 tester에 저장
    tester = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    tester_num = [0]*3 # 점수 저장
    idx= [0, 0, 0] # 문제의 답을 가르치는 idx 값
    for a in range(len(answers)):
        for t in range(3):
            if answers[a] == tester[t][idx[t]]: # 답일 경우 점수 올리기
                tester_num[t] += 1
            idx[t] += 1
            if idx[0] == 5: idx[0] = 0
            if idx[1] == 8: idx[1] = 0
            if idx[2] == 10: idx[2] = 0

    # 가장 높은 점수를 받은 사람 저장하여 출력
    max_num = max(tester_num)
    for tn in range(len(tester_num)):
        if tester_num[tn] == max_num:
            answer.append(tn+1)
    return answer


# answers = [1, 3, 2, 4, 2] 
# print(solution(answers)) # [1, 2, 3]