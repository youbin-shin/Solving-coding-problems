testcase = int(input())

for tc in range(testcase):
    N = int(input())
    file = ''
    print('#{}'.format(tc + 1))
    for i in range(N):
        text, num = map(str, input().split())
        num = int(num)
        for i in range(num):
            file += text
            if len(file) == 10:
                print(file)
                file = ''

    print(file)