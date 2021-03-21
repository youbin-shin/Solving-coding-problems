tc = int(input())

for i in range(tc):
    row = int(input())
    result = 0
    for r in range(row):
        seat1, seat2 = map(int, input().split())
        result += seat2 - seat1 + 1

    print('#{} {}'.format(i+1, result))