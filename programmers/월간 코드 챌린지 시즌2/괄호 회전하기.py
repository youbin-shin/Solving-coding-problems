from collections import deque

def solution(s):
    answer = 0
    s = deque(s)
    len_s = len(s)

    def is_right_s(test_s): # 올바른  괄호 문자열인지 확인하는 함수
        q = []
        front = ["{", "[", "("]
        back_dict = {"}": "{", "]": "[", ")": "("}
        is_right = True
        for t in test_s:
            if t not in front:
                if q != [] and q[-1] == back_dict[t]:
                    q.pop()
                else: # 올바르지 않은 문자열의 조건
                    is_right = False
                    break
            else:
                q.append(t)
        if q: # 올바르지 않은 문자열의 조건
            is_right = False
        return is_right

    for i in range(len_s):
        s.append(s.popleft())
        if is_right_s(s):
            answer += 1
    return answer
