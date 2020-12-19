from collections import deque

def solution(people, limit):
    answer = 0
    people.sort() # 오름차순
    people = deque(people)
    weight = people.pop()
    while people:
        if weight + people[0] <= limit: # 구명보트에 태울 수 있는 경우
            weight += people.popleft()
        else: # 구명보트에 탈 사람이 정해진 경우
            answer += 1
            weight = people.pop()
    if weight: # 보트에 아직 타지 못한 사람이 있는 경우
        answer += 1
    return answer


# people = [70, 50, 80, 50]
# limit = 100
# print(solution(people, limit))