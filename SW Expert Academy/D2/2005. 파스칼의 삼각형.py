def combination(a,b):
    result = 1
    for _ in range(b):
        result *= a
        a -= 1
    for _ in range(b):
        result /= b
        b -= 1
    return int(result)

tc = int(input())
for t in range(tc):
    num = int(input())
    print('#{}'.format(t+1))
    for i in range(num):
        for j in range(0, i+1):
            print(combination(i,j), end=' ')
        print()


# # solution 2
# testcase = int(input())

# for tc in range(testcase):
#     N = int(input())
#     pascal = [[1] for _ in range(N)]
#     for i in range(1, N):
#         pascal[i] = [1] * (i+1)

#     if N > 2:
#         for i in range(2, N):
#             for j in range(1, i):
#                 pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
#     print('#{}'.format(tc+1))

#     for i in range(N):
#         for j in range(i+1):
#             print(pascal[i][j],end=' ')
#         print()