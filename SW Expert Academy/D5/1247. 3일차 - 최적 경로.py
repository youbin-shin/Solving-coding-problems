def perm(k, N):
    if k == N: func(arr)
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm(k + 1, N)
            arr[k], arr[i] = arr[i], arr[k]

def func(arr):
    global shortest
    distance = abs(start[0] - gogaek[2*arr[0]]) + abs(start[1] - gogaek[2*arr[0]+1])
    for i in range(1, len(arr)):
        distance += abs(gogaek[2*arr[i]] - gogaek[2*arr[i-1]]) + abs(gogaek[2*arr[i]+1] - gogaek[2*arr[i-1]+1])
        if distance > shortest:
            break
    distance += abs(home[0] - gogaek[2*arr[-1]]) + abs(home[1] - gogaek[2*arr[-1]+1])
    if shortest > distance:
        shortest = distance
        return


for t in range(1, int(input())+1):
    # 입력
    N = int(input())
    xylist = list(map(int, input().split()))
    start = []
    home = []
    distance = 0
    shortest = 1000000000000000
    gogaek = []
    j = 0
    for i in range(0, len(xylist)-1, 2):
        if i == 0:
            start.append(xylist[i])
            start.append(xylist[i+1])
        elif i == 2:
            home.append(xylist[i])
            home.append(xylist[i+1])
        else:
            gogaek.append(xylist[i])
            gogaek.append(xylist[i+1])
            j += 1
    # 순열 만들기
    arr = [x for x in range(N)]
    perm(0, N)   
    print('#{} {}'.format(t, shortest))