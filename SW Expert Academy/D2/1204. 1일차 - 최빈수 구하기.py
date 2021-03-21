T = int(input())

for tc in range(T):
    tc_num = int(input())
    numbers = list(map(int, input().split()))

    cnt = 0
    manyvalue = 0
    for i in range(1, 101):
        if cnt <= numbers.count(i):
            cnt = numbers.count(i)
            manyvalue = i

    print('#{} {}'.format(tc_num, manyvalue))