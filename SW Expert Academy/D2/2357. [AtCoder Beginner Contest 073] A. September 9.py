tc = int(input())

for i in range(tc):
    num = input()
    for n in num:
        if n == '9':
            result = 'Yes'
            break
    else:
        result = 'No'

    print('#{} {}'.format(i+1, result))