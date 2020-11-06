def solution(begin, target, words):
    answer = 0
    length = len(begin)
    if target in words: # 단어 변환이 가능한 경우
        visited = [0] * len(words)
        q = []
        q.append(begin)
        while q:
            if target in q: # target 이 q 안에 있을 경우 종료
                break
            temp = q.pop()
            for i in range(len(words)):
                if visited[i] == 0:
                    cnt = 0
                    for j in range(length):
                        if temp[j] == words[i][j]:
                            cnt += 1
                    if cnt == length - 1: # 단어 변환이 가능한 경우 q에 추가
                        q.append(words[i])
                        visited[i] = 1
            answer += 1
    return answer


begin, target, words = "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))