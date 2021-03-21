tc = int(input())
for t in range(tc):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    result =''
    for i in range(len(lst)):
        result += str(lst[i]) + ' '

    print('#{} {}'.format(t+1,result))