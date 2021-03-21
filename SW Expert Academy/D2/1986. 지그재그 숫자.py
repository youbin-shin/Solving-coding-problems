tc = int(input())
for t in range(tc):
    N = int(input())
    result = 0
    for i in range(1, N+1):
        if i%2:
            result += i
        else:
            result -= i

    print('#{} {}'.format(t+1,result))