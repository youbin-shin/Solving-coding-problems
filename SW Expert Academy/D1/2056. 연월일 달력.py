testcase = int(input())
for tc in range(testcase):
    date = input()
    year = date[0:4]
    month = date[4:6]
    day = date[6:8]

    d31 = [1, 3, 5, 7, 8, 10, 12]
    d30 = [4, 6, 9, 11]
    result = year+'/'+month+'/'+day
    
    if month == '02':
        if int(day) > 28 or int(day) < 0:
            result = -1
    elif int(month) in d31:
        if int(day) > 31 or int(day) < 0:
            result = -1
    elif int(month) in d30:
        if int(day) > 30 or int(day) < 0:
            result = -1
    else:
        result = -1

    print(f'#{tc+1} {result}')