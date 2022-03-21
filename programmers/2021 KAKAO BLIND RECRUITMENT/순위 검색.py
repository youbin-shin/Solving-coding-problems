from itertools import combinations


def solution(info, query):
    answer = []

    info_dict = dict()
    for i in info: # i = "java backend junior pizza 150"
        i_list = i.split(" ")
        i_key = i_list[:-1] # ['java', 'backend', 'junior', 'pizza']
        i_value = i_list[-1] # 150

        # i_key로 만들 수 있는 모든 경우 info_dict에 저장
        for num in range(5):
            for c in combinations(i_key, num):
                key = "".join(c)
                if key in info_dict:
                    info_dict[key].append(int(i_value))
                else:
                    info_dict[key] = [int(i_value)]

    for id in info_dict:
        info_dict[id].sort()

    for q in query:
        q_list = q.split(" ")
        while "and" in q_list:
            q_list.remove("and")
        while "-" in q_list:
            q_list.remove("-")
        q_key = "".join(q_list[:-1])
        q_value = int(q_list[-1])

        res = 0
        if q_key in info_dict: # 효율성을 위해 필요
            res_list = info_dict[q_key]
            if len(res_list) > 0:
                left, right = 0, len(res_list)
                while left < right:
                    mid = (left + right) // 2
                    if res_list[mid] >= q_value:
                        right = mid
                    else:
                        left = mid + 1
                res = len(res_list) - left

        answer.append(res)
    return answer


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