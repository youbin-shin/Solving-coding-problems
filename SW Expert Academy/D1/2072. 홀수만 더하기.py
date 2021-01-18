testcase = int(input())

for tc in range(testcase):
    result = 0
    lst = list(map(int, input().split()))
    for i in lst:
        if i%2:
            result += i
    print(f'#{tc+1} {result}')