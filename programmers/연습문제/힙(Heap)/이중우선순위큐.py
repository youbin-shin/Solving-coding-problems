# solution 1) heapq 활용
import heapq

def solution(operations):
    hq = []
    for op in operations:
        op1, op2 = op.split(" ")
        op2 = int(op2)
        if op1 == "I":
            heapq.heappush(hq, op2)
        elif hq != []: # op1 = "D"
            if op2 == 1:
                hq = heapq.nlargest(len(hq), hq)[1:] # 최소힙에서 최대값 제거하기
                heapq.heapify(hq)
            else:
                heapq.heappop(hq)
    if hq == []: answer = [0, 0]
    else:
        answer = [heapq.nlargest(1, hq)[0], heapq.nsmallest(1, hq)[0]]
    return answer

# solution 2) 리스트 활용
def solution(operations):
    answer = []
    for op in operations:
        op1, op2 = op.split(" ")
        op2 = int(op2)
        if op1 == "I":
            answer.append(op2)
        elif answer != []: # op1 = "D"
            if op2 == 1:
                answer.pop(answer.index(max(answer)))
            else:
                answer.pop(answer.index(min(answer)))
    if answer == []: answer = [0, 0]
    else:
        answer = [max(answer), min(answer)]
    return answer
