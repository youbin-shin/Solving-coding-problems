# 정확성은 통과이지만 효율성은 실패하는 코드
def solution(info, query):
    answer = []
    query_list = [q.split(' ') for q in query]
    info_list = [i.split(' ') for i in info]
    for query_num in range(len(query_list)):
        for q in range(len(query_list[query_num]) - 1):
            query_list[query_num][q] = query_list[query_num][q][:1]
    for info_num in range(len(info_list)):
        for i in range(4):
            info_list[info_num][i] = info_list[info_num][i][:1]
    applicant_cnt = len(info)
    for q1 in query_list:
        idx = 4
        pass_list = [1 for _ in range(applicant_cnt)]
        for q2 in range(len(q1) - 1, - 1, - 1):
            if q1[q2] == 'a':
                continue
            elif q1[q2] == '-':
                idx -= 1
                continue
            for i in range(applicant_cnt):
                if pass_list[i]:
                    if q2 == len(q1) - 1:
                        if int(q1[q2]) > int(info_list[i][-1]):
                            pass_list[i] = 0
                    elif q1[q2] != info_list[i][idx]:
                        pass_list[i] = 0
            idx -= 1

        answer.append(pass_list.count(1))
    return answer