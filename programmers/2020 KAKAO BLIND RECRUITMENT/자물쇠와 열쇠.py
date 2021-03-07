from copy import deepcopy

def solution(key, lock):
    answer = False
    M, N = len(key), len(lock)
    board = [[0] * (N + (M - 1) * 2) for _ in range(N + (M - 1) * 2)]
    start = [M - 1, M - 1] # board에 lock부분 시작 좌표 저장
    # board 중앙에 lock 위치시키기
    for ly in range(N):
        for lx in range(N):
            board[start[0] + ly][start[1] + lx] = lock[ly][lx]
    # key를 움직이며 완전 탐색 진행하기
    for r in range(4): # key 회전시키기
        for y in range(len(board) - (M - 1)):
            if answer: break
            for x in range(len(board) - (M - 1)):
                test_board = deepcopy(board)
                flag = False
                # key 위치 저장하기
                for ky in range(M):
                    for kx in range(M):
                        test_board[y + ky][x + kx] += key[ky][kx]
                # lock 부분 확인하기 => 모두 1이면 answer = true (종료조건)
                for ty in range(N):
                    if flag: break
                    for tx in range(N):
                        if test_board[start[0] + ty][start[1] + tx] != 1:
                            flag = True
                            break
                if flag == False:
                    answer = True
                    break
        if r != 3: # key 시계 방향으로 90도 회전시키기
            rotate_key = [[0] * M for _ in range(M)]
            for ry in range(M):
                for rx in range(M):
                    rotate_key[rx][M - ry - 1] = key[ry][rx]
            key = deepcopy(rotate_key)

    return answer


# key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# print(solution(key, lock))