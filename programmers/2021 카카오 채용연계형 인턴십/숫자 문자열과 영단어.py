def solution(s):
    answer = ''
    str_dict = {
        'ze': ['0', 3], 'on': ['1', 2], 'tw': ['2', 2], 'th': ['3', 4], 'fo': ['4', 3],
        'fi': ['5', 3], 'si': ['6', 2], 'se': ['7', 4], 'ei': ['8', 4], 'ni': ['9', 3]
    }

    pass_cnt = 0
    for i in range(len(s)):
        if pass_cnt:
            pass_cnt -= 1
            continue
        if s[i] in [str(j) for j in range(10)]:
            answer += s[i]
        else:
            en = s[i:i + 2]
            number, pass_cnt = str_dict[en]
            answer += number

    return int(answer)