def work(day, value):
    global final_value, N
    if day == N:
        # 퇴사날이 되면 최대 수익과 비교하기
        if value > final_value:
            final_value = value
        return
    if day + table[day][0] <= N: # 상담이 가능한 경우에
        # day 인 날에 상담을 받는 경우
        work(day+table[day][0], value + table[day][1])
    # day 인 날에 상담을 안받는 경우
    work(day+1, value)


N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
final_value = 0
work(0, 0)
print(final_value)


# 다른 풀이 (시간더빠름)
# def work(day, income):
#     global final_income
#     if day < N:
#         work(day + consulting[day][0], income + consulting[day][1]) # 상담할 경우
#         work(day + 1, income) # 상담안할 경우
#     if day <= N:
#         if final_income < income:
#             final_income = income


# N = int(input())
# consulting = [list(map(int, input().split())) for _ in range(N)]
# final_income = 0
# work(0, 0)
# print(final_income)