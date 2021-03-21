testcase = int(input())

for tc in range(testcase):
    sentence = input()
    print(sentence)
    for i in range(1, 10):
        if sentence[0:i] == sentence[i:i+i]:
            result = i
            break

    print('#{} {}'.format(tc+1, result))