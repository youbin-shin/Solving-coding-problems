# sol 1
def rotation(lst, N): # 90도 회전
    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[i][j] = lst[N-j-1][i]
    return result

T = int(input())

for tc in range(T):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]

    lst1 = rotation(numbers, N)
    lst2 = rotation(lst1, N)
    lst3 = rotation(lst2, N)

    print('#{}'.format(tc+1))

    for i in range(N):
        result = ''
        for j in range(N):
            result += str(lst1[i][j])
        result += ' '
        for j in range(N):
            result += str(lst2[i][j])
        result += ' '
        for j in range(N):
            result += str(lst3[i][j])

        print(result)


# # sol 2
# testcase = int(input())

# def rotate(lst,N):
#     result = [[0 for _ in range(N)] for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             result[i][j] = lst[N-j-1][i]
#     return result

# for tc in range(testcase):
#     N = int(input())
#     lst = [[0 for _ in range(N)] for _ in range(N)]
#     for i in range(N):
#         lst[i] = list(map(int, input().split()))

#     lst_1 = rotate(lst, N)
#     lst_2 = rotate(lst_1, N)
#     lst_3 = rotate(lst_2, N)

#     for i in range(N):
#         for j in range(N):
#             lst_1[i][j] = str(lst_1[i][j])
#             lst_2[i][j] = str(lst_2[i][j])
#             lst_3[i][j] = str(lst_3[i][j])


#     print('#{}'.format(tc+1))

#     for i in range(N):
#         print(''.join(lst_1[i]),end=' ')
#         print(''.join(lst_2[i]),end=' ')
#         print(''.join(lst_3[i]),end=' ')
#         print()