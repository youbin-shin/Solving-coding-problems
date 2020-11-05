from math import gcd

def solution(arr):
  answer = arr[0]
  for a in arr[1:]:
    answer = int(answer * a / gcd(answer, a))
  return answer


arr = [2,6,8,14]
print(solution(arr))