def cal(n, N, V, op1, op2, op3, op4):
    global minV, maxV
    if n == N:
        if V < minV:
            minV = V
        if V > maxV: # elif 사용하면 X
            maxV = V
    else:
        if op1 > 0:
            cal(n+1, N, V+nums[n], op1-1, op2, op3, op4)
        if op2 > 0:
            cal(n+1, N, V-nums[n], op1, op2-1, op3, op4)
        if op3 > 0:
            cal(n+1, N, V*nums[n], op1, op2, op3-1, op4)
        if op4 > 0:
            cal(n+1, N, int(V/nums[n]), op1, op2, op3, op4-1)

for t in range(1, int(input())+1):
    N = int(input())
    op1, op2, op3, op4 = map(int, input().split())
    nums = list(map(int, input().split()))
    minV = 100000000; maxV = -100000000
    cal(1, N, nums[0], op1, op2, op3, op4)
    print('#{} {}'.format(t, maxV-minV))