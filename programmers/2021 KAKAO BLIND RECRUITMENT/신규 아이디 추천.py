from collections import deque

def solution(new_id):
    new_id = new_id.lower() # 1단계
    answer = deque()
    cnt = 0
    for n in new_id: # 2단계
        if n.isalpha() or n.isdigit() or n in ["-", "_"]:
            answer.append(n)
            cnt = 0
        if n == "." and cnt == 0: # 3단계
            answer.append(n)
            cnt += 1
    while answer and answer[0] == ".": # 4단계
        answer.popleft()
    while answer and answer[-1] == ".": # 4단계
        answer.pop()
    if len(answer) == 0: # 5단계
        answer.append("a")
    if len(answer) >= 16: # 6단계
        answer = list("".join(answer)[:15])
        while answer[-1] == ".":
            answer.pop()
    if len(answer) <= 2: # 7단계
        while len(answer) < 3:
            answer.append(answer[-1])
    return "".join(answer)


new_id = "=.="
print(solution(new_id))