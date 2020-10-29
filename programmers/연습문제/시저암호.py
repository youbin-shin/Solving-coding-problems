def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if ord("A") <= ord(s[i]) <= ord("Z"): # 대문자인 경우
            temp = int(ord(s[i])) + n
            if temp > ord("Z"):
                temp = int(temp) - int(ord("Z")) + 64
            answer += chr(temp)
        elif ord("a") <= ord(s[i]) <= ord("z"): # 소문자인 경우
            temp = int(ord(s[i])) + n
            if temp > ord("z"):
                temp = int(temp) - int(ord("z")) + 96
            answer += chr(temp)
        else: # 공백인 경우
                answer += " "
    return answer


# s = "AB"
# n = 1
# print(solution(s, n))