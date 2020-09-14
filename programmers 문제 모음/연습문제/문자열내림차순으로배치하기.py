def solution(s):
    s = list(s)
    s.sort(reverse=True) # list로 바꿔 내림차순으로 정렬
    answer = "".join(s) # 문자열로 고치기
    return answer

# s = "Zbcdefg"
# print(solution(s))