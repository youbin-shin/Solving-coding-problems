def solution(s):
    answer = ''
    first_check = True # 대문자여야 하는 경우를 저장하는 변수
    for i in range(len(s)):
        if s[i] == " ": # 공백인 경우
            first_check = True # 다음 글자 대문자로 만들기 위해 True 저장
            answer += " "
        elif first_check: # 대문자여야 하는 경우
            answer += s[i].upper()
            first_check = False 
        else: # 소문자여야 하는 경우
            answer += s[i].lower()
    return answer


# s = "3people unFollowed me"
# print(solution(s))