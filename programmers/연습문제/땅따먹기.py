def solution(land):
    N = len(land)
    for n in range(N - 1): # DB 이용 : 다른 열의 최대값을 더해가며 계산
        land[n + 1][0] += max(land[n][1], land[n][2], land[n][3])
        land[n + 1][1] += max(land[n][0], land[n][2], land[n][3])
        land[n + 1][2] += max(land[n][0], land[n][1], land[n][3])
        land[n + 1][3] += max(land[n][0], land[n][1], land[n][2])
    return max(land[-1])


# land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
# print(solution(land))