testcase = int(input())

for tc in range(testcase):
    lst = list(map(int, input().split()))
    result = lst[0]
    for i in range(1, len(lst)):
        if result < lst[i]:
            result = lst[i]
    print(f'#{tc+1} {result}')