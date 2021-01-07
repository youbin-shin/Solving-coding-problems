def solution(arr):
    answer = []
    # 분할 정복 이용
    def compress(x, y, n):
        check = arr[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):
                if check != arr[i][j]: # 영역의 값이 같지 않으면 나누기
                    compress(x, y, n // 2)
                    compress(x, y + n // 2, n // 2)
                    compress(x + n // 2, y, n // 2)
                    compress(x + n // 2, y + n // 2, n // 2)
                    return # 꼭 해주기!
        answer.append(check)
        
    compress(0, 0, len(arr))
    return [answer.count(0), answer.count(1)]


# arr = [[1,1,0,0],[1,0,0,0],[1,0,1,1],[1,1,1,1]]
# arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
# print(solution(arr))