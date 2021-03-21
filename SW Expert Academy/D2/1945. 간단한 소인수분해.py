tc = int(input())
for t in range(tc):
    num = int(input())
    factor = [2, 3, 5, 7, 11]
    result = [0, 0, 0, 0, 0]

    for i in range(5):
        count = 0
        while True:
            if num % factor[i] == 0:
                count += 1
                num = num//factor[i]
            else:
                result[i] = count
                break
    print('#{} '.format(t+1),end='')
    for j in range(5):
        print('{}'.format(result[j]),end=' ')
    print()