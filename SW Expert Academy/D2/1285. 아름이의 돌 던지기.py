T = int(input())

for tc in range(T):
    people = int(input())
    stone = list(map(int, input().split()))

    distance = 100000
    num_people = 0

    # 0 과 가까운 거리 찾기
    for i in range(people):
        if abs(stone[i]) < distance:
            distance = abs(stone[i])


    # 사람 수 찾기
    num_people += stone.count(distance) + stone.count(-distance)


    print('#{} {} {}'.format(tc+1, distance, num_people))