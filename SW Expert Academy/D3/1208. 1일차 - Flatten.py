for j in range(1, 11):
    # 입력
    dump = int(input())
    box = list(map(int, input().split()))

    # 계산
    for i in range(dump):
        maxindex = box.index(max(box))
        minindex = box.index(min(box))
        box[maxindex] = box[maxindex] -1
        box[minindex] = box[minindex] +1
        if (max(box) - min(box)) <= 1:
            break

    # 출력
    print(f'#{j} {max(box)-min(box)}')