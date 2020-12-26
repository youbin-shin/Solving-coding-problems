def solution(A, B):
    answer = 0
    A = sorted(A) # A 오름차순으로 정렬
    B = sorted(B, reverse=True) # B 내림차순으로 정렬
    N = len(A)
    for n in range(N):
        answer += A[n] * B[n]
    return answer


# A = [1, 4, 2]
# B = [5, 4, 4]
# print(solution(A,B))