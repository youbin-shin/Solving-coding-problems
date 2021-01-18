testcase = int(input())

for tc in range(testcase):
    result = 0
    lst = list(map(int, input().split()))
    for i in lst:
        result += i
    result = int(round(result/10,0))
    print(f'#{tc+1} {result}')