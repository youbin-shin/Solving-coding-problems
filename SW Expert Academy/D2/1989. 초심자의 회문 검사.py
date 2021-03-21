tc = int(input())

for i in range(1, tc+1):
    # 입력
    word = input()
    result = 0
    # 계산
    if word == word[::-1]:
        result = 1
    else:
        result = 0

    # 출력
    print('#{} {}'.format(i, result))