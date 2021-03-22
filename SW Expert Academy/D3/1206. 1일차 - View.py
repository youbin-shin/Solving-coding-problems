def func(lst):
    count = 0
    for i in range(2, len(lst)-1):
        for j in range(lst[i],0,-1):
            if j > lst[i-1] and j > lst[i-2] and j > lst[i+1] and j > lst[i+2]:
                count += 1
    return count

test_case = 10

for i in range(1, (test_case)+1):
    # 입력
    N = int(input())
    Bs = list(map(int, input().split()))
    result = 0

    # 계산
    result += func(Bs)

    # 출력
    print('#{} {}'.format(i, result))