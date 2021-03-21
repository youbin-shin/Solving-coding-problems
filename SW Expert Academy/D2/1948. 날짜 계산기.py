T = int(input())

for tc in range(T):
    m1, d1, m2, d2 = map(int, input().split())
    monthday = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day = 0

    for i in  range(m1, m2+1):
        if i == m1:
            day += monthday[m1] - d1 + 1
        elif i == m2:
            day += d2
        else:
            day += monthday[i]

    print('#{} {}'.format(tc+1, day))