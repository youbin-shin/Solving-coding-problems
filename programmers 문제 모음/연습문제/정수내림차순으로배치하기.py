def solution(n):
    n = list(str(n)) # 문자형태로 리스트로 저장
    n.sort(reverse=True) # 내림차순 정렬
    n = "".join(n) # 문자열로 합치기
    return int(n)


# n = 118372
# print(solution(n))