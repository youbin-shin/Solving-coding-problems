testcase = int(input())

for _ in range(testcase):
    tc, length = map(str, input().split())
    length = int(length)
    str_lst = list(map(str, input().split()))
    planet_lst = ['ZRO', 'ONE', 'TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
    num_lst = list()

    for i in range(10):
        num_lst.append(str_lst.count(planet_lst[i]))

    print('{}'.format(tc))

    for j in range(10):
        print('{}'.format((planet_lst[j]+' ')*num_lst[j]), end=' ')