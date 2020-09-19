def solution(s):
    answer = len(s)
    word_list = [] # 문자열을 1개 이상의 단위로 자르는 경우를 모두 저장할 리스트

    # 문자열을 1개 부터 (전체 길이 -1)개 까지 잘라서 word_list에 저장
    for i in range(1, len(s)):
        temp = []
        for j in range(0, len(s), i):
            word = s[j:j+i]
            temp.append(word)
        word_list.append(temp)

    # 문자열 압축 과정
    for w in range(len(word_list)):
        result = "" # 압축 결과 저장
        num = 1 # 압축시 문자 반복을 카운트할 변수
        words = word_list[w] # word_list 중 하나의 리스트를 뽑아 압축
        idx = 1
        end = len(words)
        word = words[0]
        while idx < end:
            if word == words[idx]: # 이전 문자와 같을 경우 num 증가
                num += 1
            else: # 이전 문자와 같지 않을 경우 result에 저장
                if num > 1: # num 2 이상인 경우
                    result += str(num) + word
                    num = 1
                else: # 반복이 일어나지 않은 경우
                    result += word
                word = words[idx]
            idx += 1
            if idx == end: # 마지막 idx확인할 경우 저장
                if num > 1:
                    result += str(num) + word
                    break
                else:
                    result += word
        # 압축한 문자열의 길이가 answer보다 작은 경우 저장
        if answer > len(list(result)):  
            answer = len(list(result))
    return answer


# s = "aabbaccc"
# print(solution(s))
