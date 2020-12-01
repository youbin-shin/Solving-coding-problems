def solution(brown, yellow):
    answer = []
    sum = brown + yellow
    for row in range(2, sum):
        if sum % row == 0: 
            col = (sum // row)
            if row >= col: # 가로 길이가 세로 길이와 같거나 길어야 하는 조건
                temp = (row - 2) * (col - 2) # 현재 카펫의 노란 영역 계산
                if temp == yellow: # 현재 카펫의 yellow 영역이 같으면 정답
                    answer = [row, col]
                    break
    return answer


# brown = 10
# yellow = 2
# print(solution(brown, yellow))