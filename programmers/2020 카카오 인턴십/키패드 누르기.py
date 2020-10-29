def solution(numbers, hand):
    answer = ''
    dial = [[3, 1], [0, 0], [0, 1], [0, 2], # 각 숫자별 위치를 저장한 리스트
            [1, 0], [1, 1], [1, 2],
            [2, 0], [2, 1], [2, 2]]
    L_thumb, R_thumb = [3, 0], [3, 2] # 두 엄지의 위치 저장
    for num in numbers:
        if num in [1, 4, 7]: # 왼쪽 엄지손가락이 누르는 경우
            answer += "L"
            L_thumb = dial[num]
        elif num in [3, 6, 9]: # 오른쪽 엄지손가락이 누르는 경우
            answer += "R"
            R_thumb = dial[num]
        else:
            # 두 엄지손가락의 거리 비교
            L_distance = abs(dial[num][0] - L_thumb[0]) + abs(dial[num][1] - L_thumb[1])
            R_distance = abs(dial[num][0] - R_thumb[0]) + abs(dial[num][1] - R_thumb[1])
            if L_distance > R_distance:
                answer += "R"
                R_thumb = dial[num]
            elif L_distance == R_distance:
                if hand == "right":
                    answer += "R"
                    R_thumb = dial[num]
                else:
                    answer += "L"
                    L_thumb = dial[num]
            else:
                answer += "L"
                L_thumb = dial[num]
    return answer


# numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# hand = "right"
# print(solution(numbers, hand))