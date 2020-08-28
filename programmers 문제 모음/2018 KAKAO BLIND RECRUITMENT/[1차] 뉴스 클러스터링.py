def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    str1_list = []
    str2_list = []
    # 각 문자열 다중집합으로 만들기
    for i in range(len(str1)-1):
        temp = str1[i:i+2]
        if temp.isalpha():
            str1_list.append(temp)
    for j in range(len(str2)-1):
        temp = str2[j:j + 2]
        if temp.isalpha():
            str2_list.append(temp)

    str1_length = len(str1_list)
    str2_length = len(str2_list)

    visited = [0] * str1_length
    intersection = 0 # 교집합의 개수

    # 두집합다 공집합일 경우 0으로 나눌 수 없기에 분기
    if str1_length == 0 and str2_length == 0: 
        result = 1
    else:
        # 교집합의 개수 구하기
        for a in range(str2_length):
            for b in range(str1_length):
                if str1_list[b] == str2_list[a] and visited[b] == 0:
                    intersection += 1
                    visited[b] = 1 # 중복 원소가 있기에 visited로 구분
                    break
        result = intersection / (str1_length + str2_length - intersection)


    answer = int(result * 65536)
    return answer

# str1 = "aa1+aa2"
# str2 = "AAAA12"
# print(solution(str1, str2))