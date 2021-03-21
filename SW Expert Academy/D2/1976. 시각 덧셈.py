testcase = int(input())

for tc in range(testcase):
    h1, m1, h2, m2 = map(int, input().split())
    h = h1 + h2
    m = m1 + m2

    while m > 60:
        h += 1
        m -= 60
    while h > 12:
        h -= 12

    print('#{} {} {}'.format(tc+1, h, m))