from collections import deque

def solution(msg):
    answer = []
    dictionary = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    msg = deque(msg)
    temp = ""
    while msg:
        temp += msg.popleft()
        if temp not in dictionary: # temp가 dictionary에 없는 경우
            dictionary.append(temp) # dictionary에 추가
            before_temp = temp[:-1] 
            answer.append(dictionary.index(before_temp) + 1) # dictionary에 인덱스 찾아 저장
            temp = temp[-1:] # 저장한 값 지우고 남은 알파벳 저장
    if temp:
        answer.append(dictionary.index(temp)+1)

    return answer


# msg = "KAKAO"
# print(solution(msg))