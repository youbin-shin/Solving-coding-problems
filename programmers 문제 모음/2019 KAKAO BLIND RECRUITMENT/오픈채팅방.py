def solution(record):
    answer = []
    user_info = {}

    for i in range(len(record)-1, -1, -1): # record list 뒤부터 확인
        r = list(map(str, record[i].split()))
        if r[0] == "Enter" or r[0] == "Change": # uid를 key로 name을 value로 저장
            if r[1] not in user_info.keys():
                user_info[r[1]] = r[2]

    # 원하는 메시지로 저장
    for j in range(len(record)):
        r = list(map(str, record[j].split()))
        if r[0] == "Enter":
            temp = user_info.get(r[1]) + "님이 들어왔습니다."
            answer.append(temp)
        elif r[0] == "Leave":
            temp = user_info.get(r[1]) + "님이 나갔습니다."
            answer.append(temp)
    return answer