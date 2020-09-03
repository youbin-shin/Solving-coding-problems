def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        # 10진수를 2진수로 바꾸기
        arr1_row = bin(arr1[i])[2:]
        arr2_row = bin(arr2[i])[2:]
        # 길이만큼 0 채우기
        if len(arr1_row) < n:
            diff = n - len(arr1_row)
            arr1_row = "0"*diff + arr1_row
        if len(arr2_row) < n:
            diff = n - len(arr2_row)
            arr2_row = "0"*diff + arr2_row

        # arr1_row, arr2_row 비교하여 벽이지 아닌지 row에 표시하기
        row = ""
        for j in range(n):
            if int(arr1_row[j])+int(arr2_row[j])==0:
                row += " "
            else:
                row += "#"
        answer.append(row) # 만들어진 row를 추가하기
    return answer

# n = 5
# arr1 = [9, 20, 28, 18, 11]
# arr2 = [30, 1, 21, 17, 28]
# print(solution(n, arr1, arr2))