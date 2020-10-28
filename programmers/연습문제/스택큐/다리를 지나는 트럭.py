def solution(bridge_length, weight, truck_weights):
  q = [0] * bridge_length
  q.pop(0)
  q.append(truck_weights[0])
  time = 1
  idx = 1
  while q:
    time += 1
    q.pop(0)
    if idx < len(truck_weights):
      if sum(q) + truck_weights[idx] > weight:
        q.append(0)
      else:
        q.append(truck_weights[idx])
        idx += 1
    else:
      time += len(q)
      break
  return time


# bridge_length = 2
# weight = 10
# truck_weights = [7,4,5,6]
# print(solution(bridge_length, weight, truck_weights))