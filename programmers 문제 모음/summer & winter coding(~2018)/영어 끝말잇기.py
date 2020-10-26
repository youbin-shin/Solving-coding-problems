def solution(n, words):
    answer = [0, 0]
    check = [] # 말한 단어를 저장할 리스트
    cnt = [0] * (n + 1)
    person = 1
    for word in words:
        cnt[person] += 1
        if word in check or len(word) == 1: # 한글자이거나 이전에 등장했던 단어일 경우 탈락
            answer = [person, cnt[person]]
            break
        elif len(check):
            if check[-1][-1] != word[0]: # 끝말잇기 규칙을 어긴 경우 탈락
                answer = [person, cnt[person]]
                break
        check.append(word)
        person += 1
        if person == n + 1:
            person = 1
    return answer


# n = 2
# words = ["hello", "one", "even", "never", "now", "world", "draw"]
# print(solution(n, words))