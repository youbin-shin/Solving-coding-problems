def solution(s):
    i = int(len(s)//2)
    if len(s) % 2: # 문자열 길이가 홀수인 경우
        answer = s[i]
    else: # 문자열 길이가 짝수인 경우
        answer = s[i-1:i+1]    
    return answer