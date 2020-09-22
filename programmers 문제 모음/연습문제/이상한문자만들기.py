def solution(s):
    answer = ''
    even = True # 짝수번째 (대문자)
    for i in range(len(s)):
        if s[i] == " ": # 공백인 경우 공백을 저장하고 다음을 짝수번째로 판단하도록 하기
            even = True
            answer += " "
        elif even: # 짝수번째 인덱스인 경우 (대문자)
            answer += s[i].upper()
            even = False
        else: # 홀수번째 인덱스인 경우 (소문자)
            answer += s[i].lower()
            even = True
    return answer


# s = "try hello world"
# print(solution(s))