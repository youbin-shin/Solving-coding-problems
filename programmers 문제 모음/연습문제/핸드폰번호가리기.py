def solution(phone_number):
    N = len(phone_number)
    answer = ''
    if N > 4: # 4보다 문자열이 큰 경우
        answer += "*" * (N-4) # 4자리를 제외한 숫자수만큼 * 추가
        answer += phone_number[-4:] # 뒷 4자리 추가
    else:
        answer = phone_number
    return answer


# phone_number = "01033334444"
# print(solution(phone_number))