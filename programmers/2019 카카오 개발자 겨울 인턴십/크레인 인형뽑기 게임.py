def solution(board, moves):
    basket = []
    length = len(board[0])
    answer = 0
    for m in moves: # 인형뽑는 경우
        for y in range(length):
            if board[y][m-1] != 0: # 인형을 뽑은 경우
                catch = board[y][m-1] # catch 변수에 뽑은 인형 저장
                board[y][m-1] = 0
                if len(basket) == 0: # 바구니가 비어있으면 catch 저장
                    basket.append(catch)
                elif basket[-1] == catch: # 바구니의 마지막 값이 catch와 같으면 없애기
                    basket.pop(-1)
                    answer += 2 # 두개의 인형이 없어졌기에 ans 2 증가
                else:
                    basket.append(catch)
                break
    return answer