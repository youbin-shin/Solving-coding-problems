import heapq

def solution(scoville, K):
  answer = 0
  heapq.heapify(scoville)
  while scoville[0] < K: # 스코빌 지수가 가장 낮은 음식이 K보다 작은 경우 실행
    answer += 1
    if len(scoville) >= 2:
      num1 = heapq.heappop(scoville)
      num2 = heapq.heappop(scoville)
      temp = num1 + num2 * 2
      heapq.heappush(scoville, temp)
    else: # 모든 음식의 스코빌 지수를 K이상으로 만들 수 없는 경우
      answer = -1
      break
  return answer


scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))