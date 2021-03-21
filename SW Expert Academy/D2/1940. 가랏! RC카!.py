T = int(input())
for tc in range(T):
    test = int(input())
    car = 0
    distance = 0
    for i in range(test):
        selection = list(map(int, input().split()))
        if selection[0] == 1:
            car += selection[1]
            distance += car
        elif selection[0] == 2:
            car -= selection[1]
            if car < 0:
                car = 0
            else:
                distance += car
        else:
            distance += car

    print('#{} {}'.format(tc+1, distance))