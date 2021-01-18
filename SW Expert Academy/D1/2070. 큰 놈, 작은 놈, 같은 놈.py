testcase = int(input())

for tc in range(testcase):
    result = ''
    lst = list(map(int, input().split()))
    if lst[0] > lst[1]:
        result = '>'
    elif lst[0] < lst[1]:
        result = '<'
    else:
        result = '='
    print(f'#{tc+1} {result}')