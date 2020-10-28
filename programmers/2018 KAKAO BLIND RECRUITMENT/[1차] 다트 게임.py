def solution(dartResult):
    score = [0] # 점수를 저장할 리스트 (-1 인덱스 에러를 피하기 위해 0을 저장해놓기)
    plus = ["S", "D", "T"]
    temp = "" # 다트 수를 저장할 변수
    idx = 0
    while idx < len(dartResult):
        while dartResult[idx].isdigit(): # temp에 문자전까지 숫자 저장
            if type(temp) == int: # 저장된 수가 있다면 score에 저장
                score.append(temp)
                temp = ""
            temp += dartResult[idx]
            idx += 1
        temp = int(temp)
        if dartResult[idx] in plus: # 보너스일 경우
            temp = temp ** (plus.index(dartResult[idx]) + 1)
        elif dartResult[idx] == "*": # 스타상인 경우
            temp *= 2
            score[-1] = score[-1] * 2
        else: # 아차상인 경우
            temp *= (-1)
        idx += 1

    score.append(temp)
    answer = sum(score)
    return answer


# dartResult = "1S2D*3T"
# dartResult = "1D2S#10S"
# print(solution(dartResult))