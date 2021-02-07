def rotateCenter(c, dir): # 해당 면 돌리기
    if dir == 1: # 시계방향
        cube[c][0], cube[c][1], cube[c][2], cube[c][3], cube[c][4], cube[c][5], cube[c][6], cube[c][7], cube[c][8] = cube[c][6], cube[c][3], cube[c][0], cube[c][7], cube[c][4], cube[c][1], cube[c][8], cube[c][5], cube[c][2]
    else: # 반시계방향
        cube[c][0], cube[c][1], cube[c][2], cube[c][3], cube[c][4], cube[c][5], cube[c][6], cube[c][7], cube[c][8] = cube[c][2], cube[c][5], cube[c][8], cube[c][1], cube[c][4], cube[c][7], cube[c][0], cube[c][3], cube[c][6]


def rotateSide(center, dir): # 주변에 있는 면 돌리기
    # side_change_list: 면을 돌리면서 돌아가야하는 면들의 인덱스를 저장한 이중리스트
    side_change_list = [
        [5, 3, 4, 2], # U면이 움직이면 돌아가야하는 주변 면의 인덱스
        [2, 4, 3, 5], # D면이 움직이면 돌아가야하는 주변 면의 인덱스
        [4, 1, 5, 0], # F면이 움직이면 돌아가야하는 주변 면의 인덱스
        [5, 1, 4, 0], # B면이 움직이면 돌아가야하는 주변 면의 인덱스
        [3, 1, 2, 0], # L면이 움직이면 돌아가야하는 주변 면의 인덱스
        [2, 1, 3, 0] # R면이 움직이면 돌아가야하는 주변 면의 인덱스
    ]

    side_list = side_change_list[center] # 변화가 필요한 면에 대한 인덱스를 저장한 리스트
    if dir == -1: # 반시계 방향일 경우 순서 거꾸로 해주기
        side_list = side_list[::-1]

    # side_index: side_change_list 면에 따른 값이 바뀌어야 하는 인덱스를 저장한 리스트 
    side_index = [
        [0, 1, 2], # U 주변 면에서 변화해야할 인덱스를 저장한 리스트
        [6, 7, 8], # D 주변 면에서 변화해야할 인덱스를 저장한 리스트
        [[2, 5, 8], [0, 1, 2], [6, 3, 0], [8, 7, 6]], # F 주변 면에서 변화해야할 인덱스를 저장한 리스트
        [[2, 5, 8], [8, 7, 6], [6, 3, 0], [0, 1, 2]], # B 주변 면에서 변화해야할 인덱스를 저장한 리스트
        [[8, 5, 2], [0, 3, 6], [0, 3, 6], [0, 3, 6]], # L 주변 면에서 변화해야할 인덱스를 저장한 리스트
        [[2, 5, 8], [2, 5, 8], [6, 3, 0], [2, 5, 8]], # R 주변 면에서 변화해야할 인덱스를 저장한 리스트
    ]

    if center in [0, 1]: # U, D 돌린 경우
        # 큐브를 돌리면서 변화해야할 인덱스 바꾸기
        # 이때 temp에 처음 면의 값을 저장해 놓고 이후 마지막 면에 temp 저장하기
        temp = [cube[side_list[0]][side_index[center][0]],
                cube[side_list[0]][side_index[center][1]],
                cube[side_list[0]][side_index[center][2]]]
        for i in range(3):
            cube[side_list[i]][side_index[center][0]], cube[side_list[i]][side_index[center][1]], cube[side_list[i]][side_index[center][2]] = cube[side_list[i + 1]][side_index[center][0]], cube[side_list[i + 1]][side_index[center][1]], cube[side_list[i + 1]][side_index[center][2]]
        cube[side_list[3]][side_index[center][0]], cube[side_list[3]][side_index[center][1]], cube[side_list[3]][side_index[center][2]] = temp[0], temp[1], temp[2]

    else: # F, B, L, R 돌린 경우
        if dir == -1: # 반시계 일 경우 순서 거꾸로 해주기
            side_index[center] = side_index[center][::-1] 

        # 큐브를 돌리면서 변화해야할 인덱스 바꾸기
        # 이때 temp에 처음 면의 값을 저장해 놓고 이후 마지막 면에 temp 저장하기
        temp = [cube[side_list[0]][side_index[center][0][0]],
                cube[side_list[0]][side_index[center][0][1]],
                cube[side_list[0]][side_index[center][0][2]]]
        for i in range(3):
            cube[side_list[i]][side_index[center][i][0]], cube[side_list[i]][side_index[center][i][1]], cube[side_list[i]][side_index[center][i][2]] = cube[side_list[i + 1]][side_index[center][i + 1][0]], cube[side_list[i + 1]][side_index[center][i + 1][1]], cube[side_list[i + 1]][side_index[center][i + 1][2]]
        cube[side_list[3]][side_index[center][3][0]], cube[side_list[3]][side_index[center][3][1]], cube[side_list[3]][side_index[center][3][2]] = temp[0], temp[1], temp[2]


test_case = int(input())
for _ in range(test_case):
    cube = [
        ["w"] * 9,  # cube[0]: U 윗면 저장
        ["y"] * 9,  # cube[1]: D 아랫면 저장
        ["r"] * 9,  # cube[2]: F 앞면 저장
        ["o"] * 9,  # cube[3]: B 뒷면 저장
        ["g"] * 9,  # cube[4]: L 왼쪽면 저장
        ["b"] * 9,  # cube[5]: R 오른쪽면 저장
    ]
    cube_center = ["U", "D", "F", "B", "L", "R"] # 입력된 면의 인덱스를 찾기 위한 리스트
    N = int(input())
    change_list = list(map(str, input().split()))
    for n in range(N):
        center, dir = cube_center.index(change_list[n][0]), change_list[n][1]
        if dir == "+": # 시계 방향
            dir = 1 
        else: # 반시계 방향
            dir = -1
        # 큐비 돌리기
        rotateCenter(center, dir) # 1. 면 돌리기
        rotateSide(center, dir) # 2. 주변에 있는 면 돌리기

    # 윗면 출력하기
    for u in range(0, 9, 3):
        for u2 in range(3):
            print(cube[0][u + u2], end="")
        print()
