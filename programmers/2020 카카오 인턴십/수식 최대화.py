from itertools import permutations
from copy import deepcopy

def solution(expression):
    answer = 0
    express_list = []
    oper = ["*", "+", "-"]
    oper_list = list(permutations(oper, 3))
    temp = ""
    # expression 리스트로 바꾸기
    for e in expression:
        if e in oper:
            if temp != "":
                express_list.append(temp)
                temp = ""
            express_list.append(e)
        else:
            temp += e
    express_list.append(temp)

    # 가능한 우선순위 계산해보기
    for o_list in oper_list: # 가능한 연산 우선순위 하나씩 확인하는 for 문
        temp = deepcopy(express_list)
        # 우선순위가 정해진 연산자 계산하기
        for o in o_list: 
            while o in temp:
                idx = temp.index(o)
                # eval : 문자열 수식 계산
                result = eval(temp[idx - 1] + temp[idx] + temp[idx + 1])
                temp = temp[:idx - 1] + temp[idx + 2:]
                temp.insert(idx - 1, str(result))
        # 절대값이 answer 보다 큰값인지 확인
        if answer < abs(int(temp[0])):
            answer = abs(int(temp[0]))

    return answer


# expression = "100-200*300-500+20"
# print(solution(expression))