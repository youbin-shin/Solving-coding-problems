testcase = int(input())

for tc in range(testcase):
    money = int(input())
    price = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = [0]*8

    for i in range(8):
        while money >= price[i]:
            result[i] += 1
            money = money - price[i]

    print('#{}'.format(tc+1))
    for i in range(8):
        print('{}'.format(result[i]), end=' ')
    print()