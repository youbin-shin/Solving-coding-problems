testcase = int(input())

num = 10000
def find_idx(number):
    x = 1
    y = 0
    lastnum = 1
    for i in range(num):
        if number <= i*(i+1)/2:
            y = i
            lastnum = int(i*(i+1)/2)
            break
    gap = lastnum - number
    x += gap
    y -= gap
    result = [x,y]
    return result

for tc in range(testcase):
    p, q = map(int, input().split())
    p = find_idx(p)
    q = find_idx(q)
    result = [p[0]+q[0],p[1]+q[1]]
    row = result[0] + result[1] - 1
    lastrow = int(row*(row+1)/2)
    finalresult = lastrow - (row - result[1])


    print('#{} {}'.format(tc + 1, finalresult))