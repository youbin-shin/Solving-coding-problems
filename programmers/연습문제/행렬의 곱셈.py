def solution(arr1, arr2):
    answer = []
    Y = len(arr1)
    X = len(arr1[0])
    X2 = len(arr2[0])
    for n in range(Y):
        temp = []
        for y in range(X2):
            result = 0
            for x in range(X):
                # print(n, y, x)
                result += arr1[n][x] * arr2[x][y]
            temp.append(result)
        answer.append(temp)
    return answer


## testcase 1
# arr1 = [[1, 2, 3], [4, 5, 6]]
# arr2 = [[1, 4], [2, 5], [3, 6]]
## testcase 2
# arr1 = [[1, 4], [3, 2], [4, 1]]
# arr2 = [[3, 3], [3, 3]]
## testcase 3
# arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
# arr2 = [[5, 4], [2, 4], [3, 1]]
## testcase 4
# arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
# arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

# print(solution(arr1, arr2))
