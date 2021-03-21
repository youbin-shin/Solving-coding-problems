tc = int(input())
for t in range(tc):
    num = list(map(int, input().split()))
    num.sort()
    num.pop(0)
    num.pop(-1)
    result = sum(num)/len(num)
    result = int(round(result, 0))


    print('#{} {}'.format(t+1,result))