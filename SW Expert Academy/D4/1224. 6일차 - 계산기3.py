T = 10
for tc in range(T):
    N = int(input())
    before = list(map(str, input()))

    after = []
    stack = []
    for i in before:
        if ord('0') <= ord(i) <= ord('9'):
            after.append(i)
        else:
            if '(' in stack:
                if i == ')':
                    while True:
                        after.append(stack.pop(-1))
                        if stack[-1] == '(':
                            break
                    stack.pop(-1)
                else:
                    if i == '+':
                        while True:
                            if stack[-1] == '(':
                                break
                            after.append(stack.pop(-1))
                    stack.append(i)

            else:
                stack.append(i)

    stack2 = []
    cal = ['+', '*']
    ans = 0
    for j in after:
        if j not in cal:
            stack2.append(j)
        else:
            a = int(stack2.pop(-1))
            b = int(stack2.pop(-1))

            if j == '+':
                ans = a + b
                stack2.append(ans)
            else:
                ans = a * b
                stack2.append(ans)


    print('#{} {}'.format(tc+1, ans))