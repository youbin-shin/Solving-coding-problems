for t in range(1, int(input()) + 1):
    N = int(input())
    rooms = [0] * 201
    for _ in range(N):
        start, end = map(int, input().split())
        if start > end:
            start, end = end, start
        if start%2 == 0:
            start -= 1
        for i in range(start, end+1, 2):
            rooms[int(i/2)] += 1

    print('#{} {}'.format(t, max(rooms)))