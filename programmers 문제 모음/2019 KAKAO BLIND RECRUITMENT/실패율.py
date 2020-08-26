def solution(N, stages):
    answer = []
    answer_list = []
    people = len(stages) # 게임을 하는 사람 수 people 변수에 저장
    for n in range(1, N+1): # 단계마다 실패율 계산하기
        go_people = 0
        no_clear_people = 0

        # 단계별 구해야할 플레이어 수 계산
        for i in range(people):
            if n < stages[i]:
                go_people += 1
            elif n == stages[i]:
                no_clear_people += 1
                go_people += 1

        # 실패율 계산
        if go_people == 0:
            failure_rate = 0
        else:
            failure_rate = no_clear_people/go_people
        
        # 단계 번호와 실패율 저장
        answer_list.append([n, failure_rate])
    
    # 실패율 내림차순으로 정렬
    answer_list = sorted(answer_list, key=lambda x:x[1], reverse=True)
    for i in range(len(answer_list)):
        answer.append(answer_list[i][0]) # 실패율 내림차순으로 단계만 저장
    return answer

# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]
# print(solution(N, stages))