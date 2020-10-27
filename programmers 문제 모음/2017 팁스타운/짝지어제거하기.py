from collections import deque

def solution(s):
  answer = 1
  s = deque(s)
  stack = deque()
  stack.append(s.popleft())
  while len(s):
    temp = s.popleft()
    if len(stack):
      if stack[-1] == temp: # 스택 마지막 값과 같으면 스택 마지막값 제거
        stack.pop()
      else: # 스택 마지막 값과 같지 않으면 스택에 추가
        stack.append(temp)
    else: # 스택이 비어있으면 스택에 추가
      stack.append(temp)
  if len(stack):
    answer = 0
  return answer


# s = "baabaa"
# print(solution(s))
