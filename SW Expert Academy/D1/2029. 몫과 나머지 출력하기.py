testcase = int(input())
for i in range(testcase):
    number = list(map(int, input().split()))
    a = number[0]
    b = number[1]
    Q = a // b
    R = a % b
    print(f'#{i+1} {Q} {R}')